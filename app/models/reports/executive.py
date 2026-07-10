from __future__ import annotations

from pydantic import Field

from app.models.base import BaseData


class ExecutiveReport(BaseData):
    """
    Final executive report generated after
    combining all specialist agents.
    """

    overall_score: int

    seo_score: int

    ux_score: int

    trust_score: int

    journey_score: int

    strategy_score: int

    copy_score: int

    persona_score: int

    executive_summary: str

    strengths: list[str] = Field(
        default_factory=list
    )

    weaknesses: list[str] = Field(
        default_factory=list
    )

    quick_wins: list[str] = Field(
        default_factory=list
    )

    roadmap: list[str] = Field(
        default_factory=list
    )