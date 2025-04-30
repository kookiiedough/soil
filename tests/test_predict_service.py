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
from pathlib import Path

import pytest

from api.predict_service import PredictionService


def test_prediction_service_initialization():
    """Test prediction service initialization."""
    service = PredictionService()
    assert service.model is not None
    assert service.scaler is not None


def test_prediction_service_predict():
    """Test prediction service prediction."""
    service = PredictionService()
    fastq_path = Path(__file__).parent.parent / "data" / "sample.fastq"
    
    result = service.predict(str(fastq_path))
    
    # Check result structure
    assert "soil_risk" in result
    assert "recommendations" in result
    assert "features" in result
    
    # Check value ranges
    assert 0 <= result["soil_risk"] <= 1
    assert isinstance(result["recommendations"], list)
    assert len(result["recommendations"]) > 0
    
    # Check features
    features = result["features"]
    assert "gc_content" in features
    assert "n_count" in features
    assert "read_length_mean" in features
    assert 0 <= features["gc_content"] <= 1
    assert features["n_count"] >= 0
    assert features["read_length_mean"] > 0


def test_prediction_service_invalid_file():
    """Test prediction service with invalid file path."""
    service = PredictionService()
    with pytest.raises(FileNotFoundError):
        service.predict("nonexistent.fastq") 