import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("❌ Gemini API key not found in .env file!")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Use the latest model
MODEL = "models/gemini-2.5-flash"

# Initialize model once for faster responses
model = genai.GenerativeModel(MODEL)

def generate_response(prompt: str) -> str:
    """
    Generate a text response from the Gemini model.
    Used for both text and voice input queries.
    """
    try:
        if not prompt or not prompt.strip():
            return "⚠️ Please say or enter something first."

        response = model.generate_content(prompt)

        if response and getattr(response, "text", None):
            return response.text.strip()
        else:
            return "⚠️ Gemini didn’t return any text response."

    except Exception as e:
        return f"❌ Error generating response from Gemini: {e}"