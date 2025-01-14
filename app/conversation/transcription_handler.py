import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
WHISPER_API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large"

class AudioToTextTranscriber:
    """Handles conversion of audio to text using Hugging Face Whisper API."""

    def __init__(self):
        self.headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

    def transcribe(self, file_path: str) -> str:
        """
        Convert the given audio file into text.

        Args:
            file_path (str): Path to the audio file.

        Returns:
            str: The transcribed text from the audio.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        try:
            with open(file_path, "rb") as audio_file:
                response = requests.post(
                    WHISPER_API_URL, headers=self.headers, files={"file": audio_file}
                )
                response.raise_for_status()

            transcription = response.json().get("text", "")
            if not transcription:
                raise ValueError("Failed to transcribe the audio.")

            return transcription
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error during transcription: {e}")

if __name__ == "__main__":
    transcriber = AudioToTextTranscriber()

    audio_path = "/Users/abhaychauhan/Downloads/audio.mp3"

    try:
        transcription = transcriber.transcribe(audio_path)
        print("Transcription Output:", transcription)
    except Exception as e:
        print("Error:", str(e))
