from typing import List

from pydantic import Field

from app.models.base import BaseSchema


class ContactData(BaseSchema):
    emails: List[str] = Field(default_factory=list)

    phone_numbers: List[str] = Field(default_factory=list)

    addresses: List[str] = Field(default_factory=list)

    social_links: List[str] = Field(default_factory=list)