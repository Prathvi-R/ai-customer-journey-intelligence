from app.embeddings.chroma_store import ChromaStore
from app.embeddings.encoder import EmbeddingEncoder

from app.models.embedding import EmbeddingChunk


class Retriever:

    def __init__(
        self,
        store: ChromaStore,
    ):

        self.store = store
        self.encoder = EmbeddingEncoder()

    ###########################################################

    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[EmbeddingChunk]:

        query_chunk = EmbeddingChunk(
            id="query",
            source="query",
            title="Query",
            content=query,
        )

        self.encoder.encode([query_chunk])

        return self.store.search(
            query_chunk.embedding,
            top_k,
        )

    ###########################################################

    def retrieve_context(
        self,
        query: str,
        top_k: int = 5,
    ) -> str:

        chunks = self.search(
            query=query,
            top_k=top_k,
        )

        if not chunks:
            return "No relevant context found."

        sections = []

        for chunk in chunks:

            section = f"""
Source: {chunk.source}
Title: {chunk.title}

{chunk.content}
"""

            sections.append(section.strip())

        return "\n\n------------------------\n\n".join(sections)