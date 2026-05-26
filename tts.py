"""
tts.py — Generate German audio using OpenAI's TTS API.

Give it a German sentence (the order), and it returns an .mp3 file path.

OpenAI TTS voices (all support German):
  - alloy   → neutral, clear
  - echo    → slightly warmer
  - fable   → expressive
  - onyx    → deep, authoritative
  - nova    → bright, friendly       ← good default for language learning
  - shimmer → soft, gentle
"""

import hashlib
from pathlib import Path
from openai import OpenAI

AUDIO_DIR = Path(__file__).parent / "audio"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_VOICE = "nova"
TTS_MODEL = "tts-1"          # tts-1-hd for higher quality (slower + pricier)


def _filename_for(text: str) -> Path:
    """
    Derive a stable filename from the text content.
    Hash the text so filenames are safe and duplicate sentences reuse the same file automatically.
    """
    digest = hashlib.md5(text.encode()).hexdigest()[:12]
    return AUDIO_DIR / f"{digest}.mp3"


def generate_audio(text: str, voice: str = DEFAULT_VOICE, speed: float = 0.8) -> str:
    """
    Generate an .mp3 file for inputted German text.
 
    - Skips generation if the file already exists (idempotent).
    - Returns the path to the .mp3 file as a string.
    """
    client = OpenAI()   # reads OPENAI_API_KEY from environment automatically
    output_path = _filename_for(text)
 
    if output_path.exists():
        return str(output_path)
     
    response = client.audio.speech.create(
        model=TTS_MODEL,
        voice=voice,
        input=text,
        response_format="mp3",
        speed=speed
    )
    output_path.write_bytes(response.content)
 
    return str(output_path)


