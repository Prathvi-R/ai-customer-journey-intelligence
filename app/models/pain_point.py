from pydantic import Field

from app.models.base import BaseData


class PainPoint(BaseData):
    """
    Represents one customer pain point
    addressed by the business.
    """

    name: str

    confidence: float = 0.0

    evidence: list[str] = Field(
        default_factory=list
    )


class PainPointData(BaseData):
    """
    Collection of inferred customer pain points.
    """

    pain_points: list[PainPoint] = Field(
        default_factory=list
    )