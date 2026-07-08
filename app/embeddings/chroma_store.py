from pathlib import Path

import chromadb
from chromadb.config import Settings

from app.models.embedding import EmbeddingChunk


class ChromaStore:
    """
    Persistent vector store backed by ChromaDB.
    """

    COLLECTION_NAME = "website_embeddings"

    def __init__(self):

        self.client = None
        self.collection = None

    def build(
        self,
        chunks: list[EmbeddingChunk],
        directory: Path,
    ):

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.client = chromadb.PersistentClient(
            path=str(directory),
            settings=Settings(
                anonymized_telemetry=False,
            ),
        )

        try:
            self.client.delete_collection(
                self.COLLECTION_NAME
            )
        except Exception:
            pass

        self.collection = self.client.create_collection(
            name=self.COLLECTION_NAME
        )

        if not chunks:
            return

        self.collection.add(
            ids=[
                chunk.id
                for chunk in chunks
            ],
            embeddings=[
                chunk.embedding
                for chunk in chunks
            ],
            documents=[
                chunk.content
                for chunk in chunks
            ],
            metadatas=[
                {
                    "source": chunk.source,
                    "title": chunk.title,
                    **chunk.metadata,
                }
                for chunk in chunks
            ],
        )

    def search(
        self,
        embedding: list[float],
        top_k: int = 5,
    ) -> list[dict]:

        if self.collection is None:
            return []

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )

        output = []

        for document, metadata, distance in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0],
        ):
            output.append(
                {
                    "content": document,
                    "metadata": metadata,
                    "distance": distance,
                }
            )

        return output

    def save(
        self,
        directory: Path,
    ):
        """
        ChromaDB persists automatically.
        """
        pass

    def load(
        self,
        directory: Path,
    ):

        self.client = chromadb.PersistentClient(
            path=str(directory),
            settings=Settings(
                anonymized_telemetry=False,
            ),
        )

        self.collection = self.client.get_collection(
            self.COLLECTION_NAME
        )