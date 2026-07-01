from typing import List

from app.models.base import BaseData


class PageData(BaseData):
    """
    Represents structured information extracted from a single webpage.
    """

    url: str

    title: str

    meta_description: str

    headings: List[str]

    paragraphs: List[str]

    buttons: List[str]

    forms: List[str]

    links: List[str]

    images: List[str]