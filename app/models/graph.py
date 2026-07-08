from pydantic import Field

from app.models.base import BaseData


class GraphNode(BaseData):
    """
    Entity in the website knowledge graph.
    """

    id: str

    label: str

    type: str

    properties: dict = Field(
        default_factory=dict
    )


class GraphEdge(BaseData):
    """
    Relationship between entities.
    """

    source: str

    target: str

    relation: str


class KnowledgeGraph(BaseData):
    """
    Website knowledge graph.
    """

    nodes: list[GraphNode] = Field(
        default_factory=list
    )

    edges: list[GraphEdge] = Field(
        default_factory=list
    )