"""
AI Configuration & Client Provider for Swarnav Tour & Travels.
Supports OpenAI (GPT-4o-mini & text-embedding-3-small) and Google Gemini.
Includes smart local fallback when API key is not yet entered.
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


# OpenAI Configuration (Primary)
OPENAI_API_KEY = get_env_var("OPENAI_API_KEY", "")
OPENAI_MODEL = get_env_var("OPENAI_MODEL", "gpt-4o-mini")
OPENAI_EMBEDDING_MODEL = get_env_var("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")

# Google Gemini Configuration (Alternative)
GEMINI_API_KEY = get_env_var("GEMINI_API_KEY", "")
GEMINI_MODEL = get_env_var("GEMINI_MODEL", "gemini-2.5-flash")
GEMINI_EMBEDDING_MODEL = "text-embedding-004"

_openai_client = None
_genai_client = None


def get_openai_client():
    """Initialize and return OpenAI client if key is configured."""
    global _openai_client
    key = get_env_var("OPENAI_API_KEY", OPENAI_API_KEY)
    if not key or key == "your_openai_api_key_here":
        return None

    if _openai_client is None:
        try:
            from openai import OpenAI
            _openai_client = OpenAI(api_key=key)
            logger.info("Initialized OpenAI client with model %s", OPENAI_MODEL)
        except Exception as exc:
            logger.error("Failed to initialize OpenAI client: %s", exc)
            return None
    return _openai_client


def get_genai_client():
    """Initialize and return Google GenAI client if key is configured."""
    global _genai_client
    key = get_env_var("GEMINI_API_KEY", GEMINI_API_KEY)
    if not key or key == "your_gemini_api_key_here":
        return None

    if _genai_client is None:
        try:
            from google import genai
            _genai_client = genai.Client(api_key=key)
            logger.info("Initialized Google GenAI client with model %s", GEMINI_MODEL)
        except Exception as exc:
            logger.error("Failed to initialize Google GenAI client: %s", exc)
            return None
    return _genai_client


def get_active_llm_provider() -> str:
    """Returns 'openai', 'gemini', or 'local' depending on available keys."""
    if get_openai_client():
        return "openai"
    if get_genai_client():
        return "gemini"
    return "local"


def is_ai_configured() -> bool:
    """Check if any cloud LLM is active."""
    return get_active_llm_provider() != "local"

