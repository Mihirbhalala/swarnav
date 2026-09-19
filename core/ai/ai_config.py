"""
AI Configuration & Client Provider for Swarnav Tour & Travels.
Supports Google Gemini (Gemini 2.5 Flash / 1.5 Flash) and text-embedding-004.
Includes smart offline fallback when GEMINI_API_KEY is not configured or during testing.
"""
import os
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

# Base project directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Read environment variables directly or via settings
def get_env_var(key: str, default: str = "") -> str:
    val = os.environ.get(key, "").strip()
    if not val:
        env_file = BASE_DIR / ".env"
        if env_file.exists():
            try:
                with open(env_file, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("#") and "=" in line:
                            k, v = line.split("=", 1)
                            if k.strip() == key:
                                val = v.strip().strip("'\"")
                                break
            except Exception as e:
                logger.warning("Could not read .env file: %s", e)
    return val or default


GEMINI_API_KEY = get_env_var("GEMINI_API_KEY", "")
GEMINI_MODEL = get_env_var("GEMINI_MODEL", "gemini-2.5-flash")
EMBEDDING_MODEL = "text-embedding-004"

# Check if Gemini client can be initialized
_genai_client = None

def get_genai_client():
    global _genai_client
    if not GEMINI_API_KEY or GEMINI_API_KEY == "your_gemini_api_key_here":
        return None

    if _genai_client is None:
        try:
            from google import genai
            _genai_client = genai.Client(api_key=GEMINI_API_KEY)
            logger.info("Initialized Google GenAI client with model %s", GEMINI_MODEL)
        except Exception as exc:
            logger.error("Failed to initialize Google GenAI client: %s", exc)
            return None
    return _genai_client

def is_ai_configured() -> bool:
    return bool(GEMINI_API_KEY and GEMINI_API_KEY != "your_gemini_api_key_here")
