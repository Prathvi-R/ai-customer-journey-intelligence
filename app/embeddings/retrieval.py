from sentence_transformers import SentenceTransformer

from app.embeddings.chroma_store import ChromaStore
from app.models.embedding import EmbeddingChunk


class Retriever:

    _encoder = SentenceTransformer(
        "BAAI/bge-small-en-v1.5"
    )

    @staticmethod
    def retrieve(
        query: str,
        vector_store: ChromaStore,
        top_k: int = 5,
    ) -> list[EmbeddingChunk]:

        embedding = Retriever._encoder.encode(
            query,
            normalize_embeddings=True,
        ).tolist()

        return vector_store.search(
            embedding,
            top_k,
        )