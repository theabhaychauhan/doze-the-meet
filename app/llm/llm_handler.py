from llm.falcon_connection import FalconLLMConnection

class LLMHandler:
    """Handler class to interact with the LLM model."""
    
    def __init__(self):
        """Initialize the handler with Falcon model connection."""
        self.model_connection = FalconLLMConnection()

    def get_response(self, query: str) -> dict:
        """Method to query the model and get the response."""
        return self.model_connection.query(query)
