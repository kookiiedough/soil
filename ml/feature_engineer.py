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
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
from Bio import SeqIO


def parse_fastq(file_path: str) -> Dict[str, Dict[str, float]]:
    """
    Parse FASTQ file and extract features for soil health prediction.
    
    Args:
        file_path: Path to the FASTQ file
        
    Returns:
        Dictionary with sample IDs as keys and feature dictionaries as values
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"FASTQ file not found: {file_path}")
    
    features = {}
    
    # Parse FASTQ file using BioPython
    for record in SeqIO.parse(file_path, "fastq"):
        # Extract sample ID from the record ID
        sample_id = record.id.split()[0]
        
        # Calculate features
        sequence = str(record.seq)
        gc_content = calculate_gc_content(sequence)
        n_count = sequence.count('N')
        read_length = len(sequence)
        
        # Store features
        features[sample_id] = {
            "gc_content": gc_content,
            "n_count": n_count,
            "read_length": read_length
        }
    
    return features


def calculate_gc_content(sequence: str) -> float:
    """
    Calculate GC content of a DNA sequence.
    
    Args:
        sequence: DNA sequence string
        
    Returns:
        GC content as a float between 0 and 1
    """
    if not sequence:
        return 0.0
    
    gc_count = sequence.count('G') + sequence.count('C')
    return gc_count / len(sequence)


def aggregate_features(features: Dict[str, Dict[str, float]]) -> pd.DataFrame:
    """
    Aggregate features from multiple reads into a single feature vector per sample.
    
    Args:
        features: Dictionary with sample IDs as keys and feature dictionaries as values
        
    Returns:
        DataFrame with aggregated features
    """
    aggregated = []
    
    for sample_id, sample_features in features.items():
        # For this simple implementation, we're just using the features directly
        # In a real-world scenario, you might want to aggregate multiple reads per sample
        aggregated.append({
            "sample_id": sample_id,
            "gc_content": sample_features["gc_content"],
            "n_count": sample_features["n_count"],
            "read_length_mean": sample_features["read_length"]
        })
    
    return pd.DataFrame(aggregated)


def engineer_features(fastq_path: str) -> pd.DataFrame:
    """
    Main function to engineer features from a FASTQ file.
    
    Args:
        fastq_path: Path to the FASTQ file
        
    Returns:
        DataFrame with engineered features ready for model prediction
    """
    # Parse FASTQ file
    features = parse_fastq(fastq_path)
    
    # Aggregate features
    df = aggregate_features(features)
    
    return df


if __name__ == "__main__":
    # Example usage
    import sys
    
    if len(sys.argv) > 1:
        fastq_path = sys.argv[1]
    else:
        fastq_path = "../data/sample.fastq"
    
    df = engineer_features(fastq_path)
    print(df.head())