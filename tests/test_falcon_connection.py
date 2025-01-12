import pytest
from unittest.mock import patch
from app.llm.connectors.falcon_connection import FalconLLMConnection


def test_falcon_connection():
    with patch('requests.post') as mock_post:
        mock_post.return_value.json.return_value = {'generated_text': 'AI explained simply.'}

        falcon = FalconLLMConnection()
        response = falcon.query("Explain AI")

        assert response['generated_text'] == 'AI explained simply.'
        mock_post.assert_called_once()