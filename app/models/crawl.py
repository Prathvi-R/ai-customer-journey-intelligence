from datetime import datetime
from typing import List, Optional

from pydantic import Field

from app.models.base import BaseSchema
from app.models.enums import ArtifactType, CrawlStatus, ErrorStage
from app.models.website import WebsiteData


class CrawlConfig(BaseSchema):
    """
    Configuration used for a crawl run.
    """

    start_url: str

    max_pages: int = 100

    max_depth: int = 5

    timeout: int = 30000  # milliseconds

    headless: bool = True

    take_screenshots: bool = True

    allowed_domains: List[str] = Field(default_factory=list)


class CrawlError(BaseSchema):
    """
    Information about a failed page.
    """

    url: str

    stage: ErrorStage

    message: str


class PageArtifact(BaseSchema):
    """
    Files generated while crawling a page.
    """

    url: str

    artifact_type: ArtifactType

    path: str


class CrawlResult(BaseSchema):
    """
    Result of an entire crawl.
    """

    status: CrawlStatus = CrawlStatus.COMPLETED

    started_at: datetime = Field(default_factory=datetime.utcnow)

    completed_at: Optional[datetime] = None

    visited_urls: List[str] = Field(default_factory=list)

    failed_urls: List[str] = Field(default_factory=list)

    errors: List[CrawlError] = Field(default_factory=list)

    artifacts: List[PageArtifact] = Field(default_factory=list)

    website_data: WebsiteData