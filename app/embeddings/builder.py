from app.embeddings.chunking import ChunkingService
from app.models.embedding import (
    EmbeddingChunk,
    EmbeddingData,
)
from app.models.website import WebsiteData


class EmbeddingBuilder:

    @staticmethod
    def build(
        website: WebsiteData,
    ) -> EmbeddingData:

        data = EmbeddingData()

        for page in website.pages:

            text = "\n".join(
                page.headings +
                page.paragraphs
            )

            chunks = ChunkingService.chunk(
                text
            )

            for index, chunk in enumerate(chunks):

                data.chunks.append(

                    EmbeddingChunk(

                        id=f"{page.url}#{index}",

                        source=page.url,

                        title=page.title,

                        content=chunk,

                        metadata={
                            "page_type":
                            page.page_type.value
                        },

                    )

                )

        return data