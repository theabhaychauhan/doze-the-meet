import pytest
from app.llm.connectors.falcon_connection import FalconLLMConnection
from app.llm.handlers.llm_handler import LLMHandler

def test_llm_handler():
    mock_falcon = FalconLLMConnection()
    mock_falcon.query = lambda x: {'generated_text': 'AI explained simply.'}

    handler = LLMHandler(model=mock_falcon)
    
    response = handler.get_response("Explain AI")
    
    assert response['generated_text'] == 'AI explained simply.'
