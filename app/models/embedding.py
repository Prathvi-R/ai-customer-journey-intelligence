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

    metadata: dict = Field(
        default_factory=dict
    )


class EmbeddingData(BaseData):
    """
    Collection of chunks ready
    for embedding generation.
    """

    chunks: list[EmbeddingChunk] = Field(
        default_factory=list
    )