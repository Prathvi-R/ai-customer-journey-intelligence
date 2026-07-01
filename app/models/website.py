from datetime import datetime

from pydantic import Field

from app.models.base import BaseData
from app.models.contact import ContactData
from app.models.page import PageData


class WebsiteData(BaseData):
    """
    Represents the structured information collected
    from an entire website.
    """

    # --------------------------------------------------
    # Website Identity
    # --------------------------------------------------

    base_url: str

    domain: str

    schema_version: str = "1.0.0"

    crawl_timestamp: datetime = Field(default_factory=datetime.utcnow)

    # --------------------------------------------------
    # Extracted Website Content
    # --------------------------------------------------

    pages: list[PageData] = Field(default_factory=list)

    navigation: list[str] = Field(default_factory=list)

    projects: list[str] = Field(default_factory=list)

    blogs: list[str] = Field(default_factory=list)

    trust_signals: list[str] = Field(default_factory=list)

    contacts: ContactData = Field(default_factory=ContactData)