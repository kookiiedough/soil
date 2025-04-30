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
import pickle
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import pandas as pd

from ml.feature_engineer import engineer_features


class PredictionService:
    """Service for making soil health predictions from FASTQ files."""
    
    def __init__(self):
        """Initialize the prediction service."""
        self.model = None
        self.scaler = None
        self._load_model()
    
    def _load_model(self):
        """Load the trained XGBoost model and scaler."""
        model_path = Path(__file__).parent.parent / "ml" / "soil_xgb.pkl"
        
        if not model_path.exists():
            raise FileNotFoundError(f"Model file not found: {model_path}")
        
        with open(model_path, "rb") as f:
            model_data = pickle.load(f)
            self.model = model_data["model"]
            self.scaler = model_data["scaler"]
    
    def predict(self, fastq_path: str) -> Dict:
        """Make a prediction based on a FASTQ file.
        
        Args:
            fastq_path: Path to the FASTQ file
            
        Returns:
            Dictionary with prediction results
        """
        # Extract features from FASTQ file
        features_df = engineer_features(fastq_path)
        
        # Prepare features for prediction
        X = features_df[["gc_content", "n_count", "read_length_mean"]]
        X_scaled = self.scaler.transform(X)
        
        # Make prediction
        soil_risk_scores = self.model.predict(X_scaled)
        
        # Calculate average soil risk score
        avg_soil_risk = float(np.mean(soil_risk_scores))
        
        # Generate recommendations based on soil risk
        recommendations = self._generate_recommendations(avg_soil_risk)
        
        # Prepare response
        result = {
            "soil_risk": avg_soil_risk,
            "recommendations": recommendations,
            "features": {
                "gc_content": float(features_df["gc_content"].mean()),
                "n_count": int(features_df["n_count"].sum()),
                "read_length_mean": float(features_df["read_length_mean"].mean())
            }
        }
        
        return result
    
    def _generate_recommendations(self, soil_risk: float) -> List[str]:
        """Generate farming recommendations based on soil risk score.
        
        Args:
            soil_risk: Soil risk score (0-1)
            
        Returns:
            List of recommendation strings
        """
        recommendations = []
        
        # Low risk (healthy soil)
        if soil_risk < 0.3:
            recommendations = [
                "Maintain current farming practices as soil health is good",
                "Consider cover crops to further enhance soil structure",
                "Implement crop rotation to maintain soil health",
                "Monitor soil moisture levels regularly"
            ]
        # Medium risk
        elif soil_risk < 0.6:
            recommendations = [
                "Add organic matter to improve soil structure",
                "Consider reducing tillage to prevent soil erosion",
                "Implement crop rotation to break pest cycles",
                "Test soil pH and adjust if necessary",
                "Monitor soil moisture and adjust irrigation accordingly"
            ]
        # High risk
        else:
            recommendations = [
                "Conduct comprehensive soil testing for detailed analysis",
                "Add organic amendments to rebuild soil structure",
                "Consider cover crops to prevent erosion and add nutrients",
                "Implement no-till or reduced tillage practices",
                "Adjust pH levels based on soil test results",
                "Consider biochar or other soil remediation techniques",
                "Consult with a soil specialist for a customized recovery plan"
            ]
        
        return recommendations


# Singleton instance
prediction_service = PredictionService()