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


@pytest.fixture
def sample_fastq_path():
    """Return the path to the sample FASTQ file."""
    return str(Path(__file__).parent.parent / "data" / "sample.fastq")


@pytest.fixture
def prediction_service():
    """Return a PredictionService instance."""
    return PredictionService() 