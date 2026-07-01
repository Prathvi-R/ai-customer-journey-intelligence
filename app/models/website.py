from pydantic import BaseModel, Field

from app.models.page import PageData
from app.models.contact import ContactInfo


class WebsiteData(BaseModel):
    base_url: str

    pages: list[PageData] = Field(default_factory=list)

    navigation: list[str] = Field(default_factory=list)

    projects: list[str] = Field(default_factory=list)

    blogs: list[str] = Field(default_factory=list)

    trust_signals: list[str] = Field(default_factory=list)

    contact: ContactInfo = Field(default_factory=ContactInfo)