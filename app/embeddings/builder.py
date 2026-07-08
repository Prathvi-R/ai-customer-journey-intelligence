from app.embeddings.chunker import TextChunker
from app.embeddings.encoder import EmbeddingEncoder

from app.models.embedding import EmbeddingData
from app.models.website import WebsiteData


class EmbeddingBuilder:

    @staticmethod
    def build(
        website: WebsiteData,
    ) -> EmbeddingData:

        embedding_data = TextChunker.chunk(
            website
        )

        encoder = EmbeddingEncoder()

        embedding_data.chunks = encoder.encode(
            embedding_data.chunks
        )

        return embedding_data