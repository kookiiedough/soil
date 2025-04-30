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

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor


def load_data(data_path: str) -> pd.DataFrame:
    """
    Load soil data from CSV file.
    
    Args:
        data_path: Path to the CSV file
        
    Returns:
        DataFrame with soil data
    """
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data file not found: {data_path}")
    
    return pd.read_csv(data_path)


def preprocess_data(df: pd.DataFrame) -> tuple:
    """
    Preprocess data for training.
    
    Args:
        df: DataFrame with soil data
        
    Returns:
        Tuple of (X_train, X_test, y_train, y_test, scaler)
    """
    # Define features and target
    features = ["gc_content", "n_count", "read_length_mean"]
    target = "soil_risk"
    
    # Split data
    X = df[features]
    y = df[target]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


def train_model(X_train, y_train) -> XGBRegressor:
    """
    Train XGBoost model for soil health prediction.
    
    Args:
        X_train: Training features
        y_train: Training target
        
    Returns:
        Trained XGBoost model
    """
    # Initialize and train XGBoost model
    model = XGBRegressor(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=3,
        random_state=42
    )
    
    model.fit(X_train, y_train)
    
    return model


def evaluate_model(model, X_test, y_test) -> float:
    """
    Evaluate model performance.
    
    Args:
        model: Trained model
        X_test: Test features
        y_test: Test target
        
    Returns:
        R-squared score
    """
    score = model.score(X_test, y_test)
    print(f"Model R-squared: {score:.4f}")
    return score


def save_model(model, scaler, output_dir: str) -> None:
    """
    Save model and scaler to disk.
    
    Args:
        model: Trained model
        scaler: Fitted scaler
        output_dir: Directory to save model and scaler
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Save model
    model_path = os.path.join(output_dir, "soil_xgb.pkl")
    with open(model_path, "wb") as f:
        pickle.dump({"model": model, "scaler": scaler}, f)
    
    print(f"Model saved to {model_path}")


def main():
    """
    Main function to train and save the soil health prediction model.
    """
    # Define paths
    current_dir = Path(__file__).parent
    data_path = current_dir.parent / "data" / "dummy_soil.csv"
    output_dir = current_dir
    
    # Load and preprocess data
    print("Loading data...")
    df = load_data(str(data_path))
    
    print("Preprocessing data...")
    X_train, X_test, y_train, y_test, scaler = preprocess_data(df)
    
    # Train model
    print("Training model...")
    model = train_model(X_train, y_train)
    
    # Evaluate model
    print("Evaluating model...")
    evaluate_model(model, X_test, y_test)
    
    # Save model
    print("Saving model...")
    save_model(model, scaler, str(output_dir))
    
    print("Done!")


if __name__ == "__main__":
    main()