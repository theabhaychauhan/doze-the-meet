import os
from dotenv import load_dotenv
from ..connectors.falcon_connection import FalconLLMConnection
from ..connectors.deepseek_connection import DeepSeekConnection

load_dotenv()

class LLMHandler:
    """Handler class to interact with the LLM model."""
    
    def __init__(self, model=None):
        """Initialize the handler with the model connection fetched from .env."""
        model_type = os.getenv("LLM_MODEL", "falcon").lower()
        if model_type == "falcon":
            self.model_connection = FalconLLMConnection()
        elif model_type == "deepseek":
            self.model_connection = DeepSeekConnection()
        else:
            raise ValueError(f"Unsupported model type: {model_type}")

    def get_response(self, query: str) -> dict:
        """Method to query the model and get the response."""
        return self.model_connection.query(query)
