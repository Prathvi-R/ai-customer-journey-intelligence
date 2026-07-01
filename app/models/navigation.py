from pydantic import Field

from app.models.base import BaseData


class NavigationNode(BaseData):

    url: str

    title: str

    page_type: str

    children: list[str] = Field(default_factory=list)


class NavigationGraph(BaseData):

    nodes: list[NavigationNode] = Field(default_factory=list)