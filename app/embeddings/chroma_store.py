from pathlib import Path

import chromadb

from app.models.embedding import EmbeddingChunk


class ChromaStore:
    """
    Persistent ChromaDB vector store.
    """

    COLLECTION_NAME = "website"

    def __init__(self):

        self.client = None
        self.collection = None

    ###########################################################

    def build(
        self,
        chunks: list[EmbeddingChunk],
        directory: Path,
    ):

        db_path = directory / "chromadb"

        self.client = chromadb.PersistentClient(
            path=str(db_path)
        )

        try:
            self.client.delete_collection(
                self.COLLECTION_NAME
            )
        except Exception:
            pass

        self.collection = self.client.create_collection(
            self.COLLECTION_NAME
        )

        if not chunks:
            return

        embeddings = [
            chunk.embedding
            for chunk in chunks
            if chunk.embedding
        ]

        documents = [
            chunk.content
            for chunk in chunks
            if chunk.embedding
        ]

        ids = [
            chunk.id
            for chunk in chunks
            if chunk.embedding
        ]

        metadatas = [
            {
                "title": chunk.title,
                "source": chunk.source,
                **chunk.metadata,
            }
            for chunk in chunks
            if chunk.embedding
        ]

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
        )

    ###########################################################

    def load(
        self,
        directory: Path,
    ):

        db_path = directory / "chromadb"

        self.client = chromadb.PersistentClient(
            path=str(db_path)
        )

        self.collection = self.client.get_collection(
            self.COLLECTION_NAME
        )

    ###########################################################

    def search(
        self,
        embedding: list[float],
        top_k: int = 5,
    ) -> list[EmbeddingChunk]:

        if self.collection is None:
            return []

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )

        output = []

        ids = results["ids"][0]
        docs = results["documents"][0]
        metas = results["metadatas"][0]

        for idx, doc, meta in zip(
            ids,
            docs,
            metas,
        ):

            output.append(

                EmbeddingChunk(

                    id=idx,

                    source=meta.get(
                        "source",
                        "",
                    ),

                    title=meta.get(
                        "title",
                        "",
                    ),

                    content=doc,

                    metadata=meta,

                    embedding=[],
                )

            )

        return output

    ###########################################################

    def save(
        self,
        directory: Path,
    ):
        """
        PersistentClient saves automatically.
        """
        pass