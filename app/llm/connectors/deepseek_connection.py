import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DeepSeekConnection:
    """Class to interact with the DeepSeek API."""
    
    def __init__(self):
        """Initialize the DeepSeekAPIConnection with API URL and authorization header."""
        self.api_url = os.getenv("DEEPSEEK_API_URL", "https://api.deepseek.com/chat/completions")
        self.api_token = os.getenv("DEEPSEEK_API_TOKEN")
        if not self.api_token:
            raise ValueError("DEEPSEEK_API_TOKEN environment variable is not set.")
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

    def query(self, user_message: str, system_message: str = "You are a helpful assistant.") -> dict:
        """
        Send a query to the DeepSeek API and return the response.

        Args:
            user_message (str): The user's input/question.
            system_message (str): The system's role description (default is a helpful assistant).

        Returns:
            dict: The response from the DeepSeek API or an error message.
        """
        if not user_message or not isinstance(user_message, str):
            raise ValueError("User message must be a non-empty string.")
        
        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            "stream": False
        }
        response = requests.post(self.api_url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def get_model_name(self) -> str:
        """Return the name of the DeepSeek model."""
        return "deepseek-chat"