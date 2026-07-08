from pydantic import Field

from app.models.base import BaseData


class BrandData(BaseData):
    """
    Represents the inferred brand identity
    of the website.
    """

    industry: str = ""

    positioning: str = ""

    tone: str = ""

    mission: str = ""

    value_propositions: list[str] = Field(
        default_factory=list
    )

    differentiators: list[str] = Field(
        default_factory=list
    )

    keywords: list[str] = Field(
        default_factory=list
    )