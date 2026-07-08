from enum import Enum

from app.models.base import BaseData


class LLMProvider(str, Enum):
    OPENAI = "openai"
    GEMINI = "gemini"
    CLAUDE = "claude"
    GROQ = "groq"
    OPENROUTER = "openrouter"
    OLLAMA = "ollama"


class TaskType(str, Enum):
    GENERAL = "general"
    REASONING = "reasoning"
    CODING = "coding"
    SUMMARIZATION = "summarization"
    EXTRACTION = "extraction"
    VISION = "vision"
    CHEAP = "cheap"
    LOCAL = "local"


class LLMModel(BaseData):

    provider: LLMProvider

    name: str

    context_window: int

    supports_vision: bool = False

    supports_json: bool = True

    cost_rank: int = 3

    reasoning_rank: int = 3

    speed_rank: int = 3