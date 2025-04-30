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
from huggingface_hub import hf_hub_download

def download_model():
    """
    Download the Llama-3-Instruct-8B-Q4_0.gguf model from Hugging Face.
    """
    # Create models directory if it doesn't exist
    models_dir = Path(__file__).parent.parent / "models"
    models_dir.mkdir(exist_ok=True)
    
    # Model details
    model_name = "Llama-3-Instruct-8B-Q4_0.gguf"
    repo_id = "TheBloke/Llama-3-Instruct-8B-GGUF"
    
    # Check if model already exists
    model_path = models_dir / model_name
    if model_path.exists():
        print(f"Model already exists at {model_path}")
        return
    
    # Download model
    print(f"Downloading {model_name} from {repo_id}...")
    try:
        hf_hub_download(
            repo_id=repo_id,
            filename=model_name,
            local_dir=str(models_dir),
            local_dir_use_symlinks=False
        )
        print(f"Model downloaded successfully to {model_path}")
    except Exception as e:
        print(f"Error downloading model: {e}")
        raise

if __name__ == "__main__":
    download_model() 