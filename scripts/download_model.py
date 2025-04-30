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
import sys
from pathlib import Path
from tqdm import tqdm
from huggingface_hub import hf_hub_download

def download_model():
    """
    Download a smaller, more accessible model for the demo.
    """
    try:
        # Create models directory if it doesn't exist
        models_dir = Path(__file__).parent.parent / "models"
        models_dir.mkdir(exist_ok=True)
        
        # Use a smaller model for demo purposes
        model_name = "phi-2.Q4_K_M.gguf"
        repo_id = "TheBloke/phi-2-GGUF"
        
        # Check if model already exists
        model_path = models_dir / model_name
        if model_path.exists():
            print(f"✅ Model already exists at {model_path}")
            return
        
        # Download model with progress bar
        print(f"📥 Downloading {model_name} from {repo_id}...")
        print("⏳ This may take a while due to the model size (~2GB)")
        print("💡 You can press Ctrl+C to cancel and continue setup")
        
        try:
            hf_hub_download(
                repo_id=repo_id,
                filename=model_name,
                local_dir=str(models_dir),
                local_dir_use_symlinks=False,
                tqdm_class=tqdm
            )
            print(f"✅ Model downloaded successfully to {model_path}")
        except KeyboardInterrupt:
            print("\n⚠️ Model download interrupted. You can run 'make setup-model' later to complete the download.")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Error downloading model: {e}")
            print("⚠️ You can still use the application without the LLM model")
            print("   Run 'make setup-model' later to retry the download")
            sys.exit(0)
            
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    download_model() 