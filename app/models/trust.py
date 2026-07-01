from pydantic import Field

from app.models.base import BaseData


class TrustSignal(BaseData):
    """
    Represents one trust indicator found
    on the website.
    """

    category: str

    value: str

    page: str


class TrustData(BaseData):
    """
    Collection of trust indicators
    across the website.
    """

    signals: list[TrustSignal] = Field(
        default_factory=list
    )

    experience_years: int | None = None

    projects_completed: int | None = None

    customers: int | None = None

    awards: list[str] = Field(
        default_factory=list
    )

    certifications: list[str] = Field(
        default_factory=list
    )