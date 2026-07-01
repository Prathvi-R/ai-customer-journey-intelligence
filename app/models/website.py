from pydantic import Field

from app.models.base import BaseData
from app.models.contact import ContactData
from app.models.journey import CustomerJourney
from app.models.navigation import NavigationGraph
from app.models.page import PageData
from app.models.cta import CTACollection


class WebsiteData(BaseData):
    """
    Represents the complete knowledge extracted
    from a website.
    """

    # --------------------------------------------------
    # Identity
    # --------------------------------------------------

    base_url: str

    domain: str

    # --------------------------------------------------
    # Pages
    # --------------------------------------------------

    pages: list[PageData] = Field(
        default_factory=list
    )

    # --------------------------------------------------
    # Website-Level Intelligence
    # --------------------------------------------------

    contacts: ContactData = Field(
        default_factory=ContactData
    )

    journey: CustomerJourney = Field(
        default_factory=CustomerJourney
    )

    navigation: NavigationGraph = Field(
        default_factory=NavigationGraph
    )

    cta: CTACollection = Field(
        default_factory=CTACollection
    )