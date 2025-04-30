from pathlib import Path
from typing import Optional
from llama_cpp import Llama
from app.core.config import settings

class LLMService:
    def __init__(self):
        self.model: Optional[Llama] = None
        self.model_path = Path(__file__).parent.parent.parent / "models" / "phi-2.Q4_K_M.gguf"
        
    def load_model(self) -> None:
        """Load the LLM model if it exists."""
        if self.model_path.exists():
            try:
                self.model = Llama(
                    model_path=str(self.model_path),
                    n_ctx=2048,  # Context window
                    n_threads=4,  # Number of CPU threads
                    n_gpu_layers=0  # CPU only for demo
                )
                print("✅ LLM model loaded successfully")
            except Exception as e:
                print(f"❌ Error loading LLM model: {e}")
                self.model = None
        else:
            print("⚠️ LLM model not found. Run 'make setup-model' to download it.")
            self.model = None
            
    def generate_response(self, prompt: str) -> str:
        """Generate a response using the LLM model."""
        if not self.model:
            return "LLM model not available. Please run 'make setup-model' to download it."
            
        try:
            response = self.model(
                prompt,
                max_tokens=512,
                temperature=0.7,
                top_p=0.95,
                repeat_penalty=1.1,
                stop=["Human:", "Assistant:"]
            )
            return response["choices"][0]["text"].strip()
        except Exception as e:
            return f"Error generating response: {str(e)}"

# Create a singleton instance
llm_service = LLMService() 