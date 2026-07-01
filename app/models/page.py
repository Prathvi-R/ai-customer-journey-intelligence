from typing import Optional

from pydantic import Field

from app.models.base import BaseData
from app.models.enums import PageType


class PageData(BaseData):
    """
    Represents a single crawled webpage.
    """

    # -------------------------
    # Identity
    # -------------------------

    url: str
    title: str = ""
    description: str = ""

    # -------------------------
    # Crawl Metadata
    # -------------------------

    page_type: PageType = PageType.OTHER

    depth: int = 0

    status_code: Optional[int] = None

    response_time_ms: Optional[float] = None

    content_hash: Optional[str] = None

    language: Optional[str] = None

    # -------------------------
    # Extracted Content
    # -------------------------

    headings: list[str] = Field(default_factory=list)

    paragraphs: list[str] = Field(default_factory=list)

    links: list[str] = Field(default_factory=list)

    images: list[str] = Field(default_factory=list)

    buttons: list[str] = Field(default_factory=list)

    forms: list[str] = Field(default_factory=list)