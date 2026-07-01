from pydantic import Field

from app.models.base import BaseData


class ContactData(BaseData):
    """
    Contact information extracted from the website.
    """

    phone_numbers: list[str] = Field(default_factory=list)

    email_addresses: list[str] = Field(default_factory=list)

    office_addresses: list[str] = Field(default_factory=list)

    social_links: list[str] = Field(default_factory=list)