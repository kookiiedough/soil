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

import pandas as pd
import pytest

from ml.feature_engineer import engineer_features, calculate_gc_content


def test_calculate_gc_content():
    """Test GC content calculation."""
    assert calculate_gc_content("") == 0.0
    assert calculate_gc_content("ATGC") == 0.5
    assert calculate_gc_content("GGCC") == 1.0
    assert calculate_gc_content("ATAT") == 0.0


def test_engineer_features():
    """Test feature engineering from FASTQ file."""
    # Get the path to the sample FASTQ file
    fastq_path = Path(__file__).parent.parent / "data" / "sample.fastq"
    
    # Engineer features
    df = engineer_features(str(fastq_path))
    
    # Check DataFrame structure
    assert isinstance(df, pd.DataFrame)
    assert "sample_id" in df.columns
    assert "gc_content" in df.columns
    assert "n_count" in df.columns
    assert "read_length_mean" in df.columns
    
    # Check data types
    assert df["gc_content"].dtype == float
    assert df["n_count"].dtype == int
    assert df["read_length_mean"].dtype == float
    
    # Check value ranges
    assert df["gc_content"].between(0, 1).all()
    assert df["n_count"].ge(0).all()
    assert df["read_length_mean"].gt(0).all()


def test_engineer_features_invalid_file():
    """Test feature engineering with invalid file path."""
    with pytest.raises(FileNotFoundError):
        engineer_features("nonexistent.fastq") 