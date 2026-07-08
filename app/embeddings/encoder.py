from sentence_transformers import SentenceTransformer

from app.models.embedding import EmbeddingChunk


class EmbeddingEncoder:

    def __init__(self):

        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def encode(
        self,
        chunks: list[EmbeddingChunk],
    ) -> list[EmbeddingChunk]:

        texts = [
            chunk.content
            for chunk in chunks
        ]

        vectors = self.model.encode(
            texts,
            normalize_embeddings=True,
        )

        for chunk, vector in zip(
            chunks,
            vectors,
        ):
            chunk.embedding = vector.tolist()

        return chunks