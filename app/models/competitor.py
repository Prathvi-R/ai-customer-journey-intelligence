from pydantic import Field

from app.models.base import BaseData


class CompetitorInsight(BaseData):
    """
    Represents inferred competitive positioning.
    """

    industry: str = ""

    market_segment: str = ""

    likely_competitors: list[str] = Field(
        default_factory=list
    )

    competitive_advantages: list[str] = Field(
        default_factory=list
    )

    differentiation_keywords: list[str] = Field(
        default_factory=list
    )