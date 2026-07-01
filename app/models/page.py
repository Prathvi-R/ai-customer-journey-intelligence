from typing import Any

from pydantic import Field

from app.models.base import BaseData
from app.models.enums import PageType


class PageData(BaseData):
    """
    Represents one crawled webpage.
    """

    # --------------------------------------------------
    # Identity
    # --------------------------------------------------

    url: str

    title: str = ""

    description: str = ""

    page_type: PageType = PageType.OTHER

    language: str = ""

    # --------------------------------------------------
    # Crawl Metadata
    # --------------------------------------------------

    depth: int = 0

    status_code: int | None = None

    response_time_ms: float | None = None

    content_hash: str | None = None

    # --------------------------------------------------
    # SEO
    # --------------------------------------------------

    canonical: str = ""

    keywords: str = ""

    robots: str = ""

    favicon: str = ""

    og_title: str = ""

    og_description: str = ""

    og_image: str = ""

    og_url: str = ""

    twitter_card: str = ""

    twitter_title: str = ""

    twitter_description: str = ""

    twitter_image: str = ""

    # --------------------------------------------------
    # Content
    # --------------------------------------------------

    headings: list[str] = Field(default_factory=list)

    paragraphs: list[str] = Field(default_factory=list)

    buttons: list[str] = Field(default_factory=list)

    forms: list[str] = Field(default_factory=list)

    images: list[str] = Field(default_factory=list)

    lists: list[list[str]] = Field(default_factory=list)

    tables: list[list[list[str]]] = Field(default_factory=list)

    # --------------------------------------------------
    # Links
    # --------------------------------------------------

    internal_links: list[str] = Field(default_factory=list)

    external_links: list[str] = Field(default_factory=list)

    mailto_links: list[str] = Field(default_factory=list)

    telephone_links: list[str] = Field(default_factory=list)

    download_links: list[str] = Field(default_factory=list)

    anchor_links: list[str] = Field(default_factory=list)

    # --------------------------------------------------
    # Structured Data
    # --------------------------------------------------

    json_ld: list[Any] = Field(default_factory=list)

    schema_types: list[str] = Field(default_factory=list)