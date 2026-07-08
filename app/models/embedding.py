from pydantic import Field

from app.models.base import BaseData


class EmbeddingChunk(BaseData):
    """
    One searchable text chunk.
    """

    id: str

    source: str

    title: str

    content: str

    embedding: list[float] = Field(
        default_factory=list
    )

    metadata: dict = Field(
        default_factory=dict
    )


class EmbeddingData(BaseData):
    """
    Collection of chunks ready
    for semantic search.
    """

    chunks: list[EmbeddingChunk] = Field(
        default_factory=list
    )