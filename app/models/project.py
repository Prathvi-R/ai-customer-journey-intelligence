from pydantic import Field

from app.models.base import BaseData


class Project(BaseData):
    """
    Represents one project, service or product
    offered by the company.
    """

    name: str

    url: str = ""

    description: str = ""

    page_type: str = ""

    images: list[str] = Field(
        default_factory=list
    )


class ProjectCatalog(BaseData):
    """
    Collection of projects found
    across the website.
    """

    projects: list[Project] = Field(
        default_factory=list
    )