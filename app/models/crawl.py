from datetime import datetime

from pydantic import Field

from app.models.base import BaseData
from app.models.enums import CrawlStatus
from app.models.website import WebsiteData


class CrawlResult(BaseData):
    """
    Represents the outcome of a crawl execution.
    """

    status: CrawlStatus = CrawlStatus.SUCCESS

    started_at: datetime

    completed_at: datetime | None = None

    pages_discovered: int = 0

    pages_crawled: int = 0

    pages_failed: int = 0

    visited_urls: list[str] = Field(default_factory=list)

    failed_urls: list[str] = Field(default_factory=list)

    website_data: WebsiteData