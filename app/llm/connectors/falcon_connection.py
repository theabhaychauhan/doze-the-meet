import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FalconLLMConnection:
    """Class to interact with the Falcon LLM model via Hugging Face API."""
    
    def __init__(self):
        """Initialize the FalconLLMConnection with API URL and authorization header."""
        self.api_url = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
        self.headers = {
            "Authorization": f"Bearer {os.getenv('HF_API_TOKEN')}"
        }

    def query(self, prompt: str) -> dict:
        """Send a query to the Falcon LLM model and return the response."""
        data = {"inputs": prompt}
        response = requests.post(self.api_url, headers=self.headers, json=data)
        return response.json()

    def get_model_name(self) -> str:
        """Return the name of the model."""
        return "Falcon 7B Instruct"
