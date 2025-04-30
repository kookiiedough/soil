# MIT License
#
# Copyright (c) 2023 Biodynamic Offline
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

import os
import shutil
from datetime import datetime
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Dict, List, Optional

from fastapi import Depends, FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlmodel import Session, select

from api.models import Prediction, User, get_session, init_db
from api.predict_service import prediction_service
from llm.rag import generate_response

# Initialize FastAPI app
app = FastAPI(
    title="Biodynamic Offline API",
    description="API for soil health prediction from FASTQ files",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database on startup
@app.on_event("startup")
def on_startup():
    init_db()


# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}


# User endpoints
@app.post("/users/", response_model=User)
def create_user(username: str = Form(...), email: str = Form(...), session: Session = Depends(get_session)):
    """Create a new user."""
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, session: Session = Depends(get_session)):
    """Get user by ID."""
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# Prediction endpoints
@app.post("/predict/")
async def predict_soil_health(
    file: UploadFile = File(...),
    user_id: Optional[int] = Form(None),
    session: Session = Depends(get_session)
):
    """Predict soil health from a FASTQ file."""
    # Validate file type
    if not file.filename.endswith(".fastq"):
        raise HTTPException(status_code=400, detail="File must be a FASTQ file")
    
    # Create temporary file
    with NamedTemporaryFile(delete=False, suffix=".fastq") as temp_file:
        # Copy uploaded file to temporary file
        shutil.copyfileobj(file.file, temp_file)
        temp_file_path = temp_file.name
    
    try:
        # Make prediction
        result = prediction_service.predict(temp_file_path)
        
        # Save prediction to database if user_id is provided
        if user_id:
            user = session.get(User, user_id)
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            
            # Create prediction record
            prediction = Prediction(
                user_id=user_id,
                file_name=file.filename,
                gc_content=result["features"]["gc_content"],
                n_count=result["features"]["n_count"],
                read_length_mean=result["features"]["read_length_mean"],
                soil_risk=result["soil_risk"]
            )
            
            session.add(prediction)
            session.commit()
            session.refresh(prediction)
            
            # Add prediction ID to result
            result["prediction_id"] = prediction.id
        
        return result
    
    finally:
        # Clean up temporary file
        os.unlink(temp_file_path)


@app.get("/predictions/{prediction_id}")
def get_prediction(prediction_id: int, session: Session = Depends(get_session)):
    """Get prediction by ID."""
    prediction = session.get(Prediction, prediction_id)
    if not prediction:
        raise HTTPException(status_code=404, detail="Prediction not found")
    
    # Generate recommendations based on soil risk
    recommendations = prediction_service._generate_recommendations(prediction.soil_risk)
    
    return {
        "id": prediction.id,
        "file_name": prediction.file_name,
        "soil_risk": prediction.soil_risk,
        "features": {
            "gc_content": prediction.gc_content,
            "n_count": prediction.n_count,
            "read_length_mean": prediction.read_length_mean
        },
        "recommendations": recommendations,
        "created_at": prediction.created_at
    }


@app.get("/users/{user_id}/predictions")
def get_user_predictions(user_id: int, session: Session = Depends(get_session)):
    """Get all predictions for a user."""
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Query predictions for user
    statement = select(Prediction).where(Prediction.user_id == user_id).order_by(Prediction.created_at.desc())
    predictions = session.exec(statement).all()
    
    return predictions


# Chat endpoint
@app.post("/chat/")
def chat(
    prediction_id: int = Form(...),
    question: str = Form(...),
    session: Session = Depends(get_session)
):
    """Generate a response to a question about soil health."""
    # Get prediction
    prediction = session.get(Prediction, prediction_id)
    if not prediction:
        raise HTTPException(status_code=404, detail="Prediction not found")
    
    # Generate recommendations based on soil risk
    recommendations = prediction_service._generate_recommendations(prediction.soil_risk)
    
    # Prepare prediction data for RAG
    prediction_data = {
        "soil_risk": prediction.soil_risk,
        "recommendations": recommendations
    }
    
    # Generate response
    response = generate_response(prediction_data, question)
    
    return {"response": response}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)