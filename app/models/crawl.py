from pydantic import Field

from app.models.base import BaseData
from app.models.website import WebsiteData


class CrawlConfig(BaseData):
    """
    Configuration used during a crawl.
    """

    max_pages: int = 25

    headless: bool = True

    timeout: int = 30000


class CrawlError(BaseData):
    """
    Represents a failed crawl attempt.
    """

    url: str

    error: str


class CrawlResult(BaseData):
    """
    Result returned after a website crawl.
    """

    visited_urls: list[str] = Field(default_factory=list)

    failed_urls: list[str] = Field(default_factory=list)

    website_data: WebsiteData