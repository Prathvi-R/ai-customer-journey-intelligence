from pydantic import Field

from app.models.base import BaseData


class AgentResult(BaseData):

    agent: str

    answer: str

    confidence: float = 1.0

    evidence: list[str] = Field(default_factory=list)