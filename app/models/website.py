from pydantic import Field

from app.models.base import BaseData
from app.models.contact import ContactData
from app.models.page import PageData


class WebsiteData(BaseData):
    """
    Represents all structured information collected
    from a single website.
    """

    base_url: str

    pages: list[PageData] = Field(default_factory=list)

    navigation: list[str] = Field(default_factory=list)

    projects: list[str] = Field(default_factory=list)

    blogs: list[str] = Field(default_factory=list)

    trust_signals: list[str] = Field(default_factory=list)

    contact: ContactData = Field(default_factory=ContactData)