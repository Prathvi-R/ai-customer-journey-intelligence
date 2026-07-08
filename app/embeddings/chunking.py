class ChunkingService:
    """
    Splits long text into
    LLM-friendly chunks.
    """

    @staticmethod
    def chunk(
        text: str,
        chunk_size: int = 800,
    ) -> list[str]:

        text = text.strip()

        if not text:
            return []

        words = text.split()

        chunks = []

        current = []

        current_length = 0

        for word in words:

            current.append(word)

            current_length += len(word) + 1

            if current_length >= chunk_size:

                chunks.append(
                    " ".join(current)
                )

                current = []

                current_length = 0

        if current:

            chunks.append(
                " ".join(current)
            )

        return chunks