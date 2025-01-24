import pytest
from unittest.mock import patch, mock_open
# from app.conversation.transcription_handler import ConversationTranscriptionHandler

# def test_transcription_handler():
#     mock_response = {"text": "This is a transcribed conversation."}

#     # Mock os.path.exists to always return True
#     with patch("os.path.exists", return_value=True), \
#          patch("builtins.open", mock_open(read_data="dummy audio data")), \
#          patch("requests.post") as mock_post:
#         # Mock the response from requests.post
#         mock_post.return_value.json.return_value = mock_response

#         transcriber = ConversationTranscriptionHandler()
#         transcription = transcriber.transcribe("dummy_path.mp3")

#         assert transcription == "This is a transcribed conversation."
#         mock_post.assert_called_once()
