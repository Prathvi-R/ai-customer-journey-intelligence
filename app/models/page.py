from typing import List

from pydantic import Field

from app.models.base import BaseSchema
from app.models.enums import PageType


class PageData(BaseSchema):
    url: str

    title: str = ""

    meta_description: str = ""

    page_type: PageType = PageType.OTHER

    headings: List[str] = Field(default_factory=list)

    paragraphs: List[str] = Field(default_factory=list)

    buttons: List[str] = Field(default_factory=list)

    forms: List[str] = Field(default_factory=list)

    links: List[str] = Field(default_factory=list)

    images: List[str] = Field(default_factory=list)