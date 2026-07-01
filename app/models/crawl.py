from pydantic import BaseModel, Field

from app.models.website import WebsiteData


class CrawlResult(BaseModel):
    visited_urls: list[str] = Field(default_factory=list)
    failed_urls: list[str] = Field(default_factory=list)

    website_data: WebsiteData