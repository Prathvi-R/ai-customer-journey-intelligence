from app.models.embedding import (
    EmbeddingChunk,
    EmbeddingData,
)
from app.models.website import WebsiteData


class TextChunker:

    MAX_PARAGRAPHS = 5

    @staticmethod
    def chunk(
        website: WebsiteData,
    ) -> EmbeddingData:

        data = EmbeddingData()

        # ----------------------------------------
        # Website Pages
        # ----------------------------------------

        for page in website.pages:

            text = "\n".join(
                page.paragraphs[
                    : TextChunker.MAX_PARAGRAPHS
                ]
            )

            data.chunks.append(
                EmbeddingChunk(
                    id=page.url,
                    source="page",
                    title=page.title,
                    content=text,
                    metadata={
                        "url": page.url,
                        "page_type": page.page_type.value,
                    },
                )
            )

        # ----------------------------------------
        # Projects / Services
        # ----------------------------------------

        if website.projects:

            for project in website.projects.projects:

                data.chunks.append(
                    EmbeddingChunk(
                        id=f"project-{project.name}",
                        source="project",
                        title=project.name,
                        content=project.description,
                        metadata={
                            "url": project.url,
                            "page_type": project.page_type,
                        },
                    )
                )

        # ----------------------------------------
        # Personas
        # ----------------------------------------

        if website.personas:

            for persona in website.personas.personas:

                evidence = "\n".join(persona.evidence)

                if not evidence:
                    evidence = persona.name

                data.chunks.append(
                    EmbeddingChunk(
                        id=f"persona-{persona.name}",
                        source="persona",
                        title=persona.name,
                        content=evidence,
                        metadata={
                            "confidence": persona.confidence,
                        },
                    )
                )

        return data