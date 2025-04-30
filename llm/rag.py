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

import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Union

from huggingface_hub import hf_hub_download
from llama_cpp import Llama

# Constants
MODEL_NAME = "Llama-3-Instruct-8B-Q4_0.gguf"
MODEL_REPO = "TheBloke/Llama-3-8B-Instruct-GGUF"
MODEL_DIR = Path("../models")
MAX_TOKENS = 256


def ensure_model_exists() -> Path:
    """
    Ensure the LLM model exists, downloading it if necessary.
    
    Returns:
        Path to the model file
    """
    model_dir = Path(__file__).parent.parent / "models"
    model_path = model_dir / MODEL_NAME
    
    if not model_path.exists():
        print(f"Model not found at {model_path}, downloading from Hugging Face...")
        os.makedirs(model_dir, exist_ok=True)
        
        # Download model from Hugging Face
        hf_hub_download(
            repo_id=MODEL_REPO,
            filename=MODEL_NAME,
            local_dir=model_dir
        )
    
    return model_path


def load_llm() -> Llama:
    """
    Load the LLM model.
    
    Returns:
        Loaded Llama model
    """
    model_path = ensure_model_exists()
    
    # Load the model with llama-cpp-python
    llm = Llama(
        model_path=str(model_path),
        n_ctx=2048,  # Context window size
        n_threads=4,  # Number of CPU threads to use
        n_gpu_layers=0  # No GPU layers for CPU-only inference
    )
    
    return llm


def create_prompt(prediction: Dict, question: str) -> str:
    """
    Create a prompt for the LLM based on soil prediction and user question.
    
    Args:
        prediction: Dictionary containing soil prediction results
        question: User's question about farming recommendations
        
    Returns:
        Formatted prompt for the LLM
    """
    # Extract soil risk and recommendations from prediction
    soil_risk = prediction.get("soil_risk", 0.5)
    recommendations = prediction.get("recommendations", [])
    
    # Format recommendations as a string
    recommendations_str = "\n".join([f"- {rec}" for rec in recommendations])
    
    # Create the prompt
    prompt = f"""<|system|>
You are an expert agricultural advisor specializing in soil health and sustainable farming practices. 
Your task is to provide helpful, accurate, and actionable advice to farmers based on soil analysis data.

Here is the soil analysis data:
- Soil Risk Score: {soil_risk} (0-1 scale, where 0 is healthy and 1 is high risk)

Recommendations from soil analysis:
{recommendations_str}

Provide a concise, practical response to the farmer's question below.
</|system|>

<|user|>
{question}
</|user|>

<|assistant|>
"""
    
    return prompt


def generate_response(prediction: Dict, question: str) -> str:
    """
    Generate a response to a user's question based on soil prediction.
    
    Args:
        prediction: Dictionary containing soil prediction results
        question: User's question about farming recommendations
        
    Returns:
        LLM-generated response
    """
    # Load the LLM
    llm = load_llm()
    
    # Create the prompt
    prompt = create_prompt(prediction, question)
    
    # Generate response
    response = llm(prompt, max_tokens=MAX_TOKENS, stop=["</|assistant|>"])
    
    # Extract the generated text
    generated_text = response["choices"][0]["text"]
    
    return generated_text.strip()


if __name__ == "__main__":
    # Example usage
    sample_prediction = {
        "soil_risk": 0.3,
        "recommendations": [
            "Add organic matter to improve soil structure",
            "Consider crop rotation to reduce pest pressure",
            "Monitor soil moisture levels regularly"
        ]
    }
    
    sample_question = "What crops would be best suited for my soil conditions?"
    
    response = generate_response(sample_prediction, sample_question)
    print(f"Question: {sample_question}\n\nResponse: {response}")