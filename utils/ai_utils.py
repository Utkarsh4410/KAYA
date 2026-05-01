# utils/ai_utils.py
import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


def get_groq_client():
    """Return an initialised Groq client.

    Key resolution order:
    1. st.secrets["GROQ_API_KEY"]  — Streamlit Community Cloud
    2. GROQ_API_KEY environment variable — local .env via python-dotenv
    """
    api_key = None

    # 1. Try Streamlit secrets (Streamlit Cloud deployment)
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except (KeyError, FileNotFoundError):
        pass

    # 2. Fall back to environment variable (local development)
    if not api_key:
        api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not found. "
            "Set it in Streamlit Cloud secrets or create a local .env file."
        )
    return Groq(api_key=api_key)


def get_ai_response(prompt, model="llama-3.3-70b-versatile"):
    """Send a prompt to the LLM and return the text response."""
    client = get_groq_client()
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=model,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


def process_voice_input(audio_data, model="whisper-large-v3-turbo"):
    """Transcribe audio using the Whisper model via Groq."""
    client = get_groq_client()
    try:
        response = client.audio.transcriptions.create(
            file=audio_data,
            model=model,
        )
        return response.text
    except Exception as e:
        return f"Error processing audio: {str(e)}"