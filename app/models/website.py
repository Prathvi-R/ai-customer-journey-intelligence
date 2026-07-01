from pydantic import Field

from app.models.base import BaseSchema
from app.models.contact import ContactData
from app.models.page import PageData


class WebsiteData(BaseSchema):
    """
    Structured representation of a collected website.
    """

    base_url: str

    pages: list[PageData] = Field(default_factory=list)

    contacts: ContactData = Field(default_factory=ContactData)