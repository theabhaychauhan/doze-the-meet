from ..connectors.falcon_connection import FalconLLMConnection
from ..connectors.deepseek_connection import DeepSeekConnection

class LLMHandler:
    """Handler class to interact with the LLM model."""
    
    def __init__(self, model=None):
        """Initialize the handler with Falcon model connection."""
        # self.model_connection = model or FalconLLMConnection()
        self.model_connection = model or DeepSeekConnection()

    def get_response(self, query: str) -> dict:
        """Method to query the model and get the response."""
        return self.model_connection.query(query)
