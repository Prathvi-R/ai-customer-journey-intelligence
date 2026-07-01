from pydantic import Field

from app.models.base import BaseData


class CTA(BaseData):
    """
    Represents one Call-To-Action discovered on the website.
    """

    text: str

    page_title: str

    page_url: str

    cta_type: str

    importance: float = 1.0


class CTACollection(BaseData):
    """
    All CTAs discovered across the website.
    """

    ctas: list[CTA] = Field(default_factory=list)

    primary_ctas: list[CTA] = Field(default_factory=list)

    secondary_ctas: list[CTA] = Field(default_factory=list)