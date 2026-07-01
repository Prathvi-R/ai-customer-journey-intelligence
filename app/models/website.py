from datetime import datetime

from pydantic import Field

from app.models.base import BaseData
from app.models.contact import ContactData
from app.models.enums import PageType
from app.models.page import PageData


class WebsiteData(BaseData):
    """
    Represents the structured information collected
    from an entire website.
    """

    base_url: str

    domain: str

    schema_version: str = "1.0.0"

    crawl_timestamp: datetime = Field(default_factory=datetime.utcnow)

    pages: list[PageData] = Field(default_factory=list)

    navigation: list[str] = Field(default_factory=list)

    projects: list[str] = Field(default_factory=list)

    blogs: list[str] = Field(default_factory=list)

    trust_signals: list[str] = Field(default_factory=list)

    contacts: ContactData = Field(default_factory=ContactData)

    @property
    def home_pages(self) -> list[PageData]:
        return [
            page
            for page in self.pages
            if page.page_type == PageType.HOME
        ]

    @property
    def about_pages(self) -> list[PageData]:
        return [
            page
            for page in self.pages
            if page.page_type == PageType.ABOUT
        ]

    @property
    def project_pages(self) -> list[PageData]:
        return [
            page
            for page in self.pages
            if page.page_type == PageType.PROJECT
        ]

    @property
    def blog_pages(self) -> list[PageData]:
        return [
            page
            for page in self.pages
            if page.page_type == PageType.BLOG
        ]