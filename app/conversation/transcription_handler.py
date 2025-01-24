from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import os
from dotenv import load_dotenv

load_dotenv()


audio_file_path = "/Users/abhaychauhan/Downloads/audio.mp3"

try:
    with open(audio_file_path, "rb") as audio_file:
        transcription = client.audio.transcribe(model="whisper-1",
        file=audio_file)
    print("Transcription Output:", transcription.text)
except Exception as e:
    print("Error:", str(e))
