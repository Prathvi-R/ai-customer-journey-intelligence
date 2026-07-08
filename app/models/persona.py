from pydantic import Field

from app.models.base import BaseData


class Persona(BaseData):
    """
    Represents one inferred customer persona.
    """

    name: str

    confidence: float = 0.0

    evidence: list[str] = Field(
        default_factory=list
    )


class PersonaData(BaseData):
    """
    Collection of customer personas.
    """

    personas: list[Persona] = Field(
        default_factory=list
    )