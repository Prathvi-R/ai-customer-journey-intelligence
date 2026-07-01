from pydantic import Field

from app.models.base import BaseData


class JourneyNode(BaseData):
    """
    Represents one page within the customer journey.
    """

    title: str

    url: str

    page_type: str

    description: str = ""

    importance: float = 1.0


class CustomerJourney(BaseData):
    """
    High-level representation of the website's
    customer acquisition funnel.
    """

    entry_pages: list[JourneyNode] = Field(default_factory=list)

    awareness_pages: list[JourneyNode] = Field(default_factory=list)

    consideration_pages: list[JourneyNode] = Field(default_factory=list)

    trust_pages: list[JourneyNode] = Field(default_factory=list)

    conversion_pages: list[JourneyNode] = Field(default_factory=list)

    support_pages: list[JourneyNode] = Field(default_factory=list)