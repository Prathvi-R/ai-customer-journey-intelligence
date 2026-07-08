from app.models.embedding import (
    EmbeddingData,
)


class EmbeddingEncoder:
    """
    Placeholder encoder.

    Later this will generate
    vector embeddings using
    Jina, Voyage, OpenAI,
    BGE, etc.
    """

    @staticmethod
    def encode(
        embeddings: EmbeddingData,
    ):

        return embeddings