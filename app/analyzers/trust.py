from app.models.page import PageData


KEYWORDS = [
    "RERA",
    "ISO",
    "award",
    "years",
    "experience",
    "trusted",
    "customers",
    "happy families",
]


class TrustAnalyzer:

    @staticmethod
    def extract(
        pages: list[PageData],
    ) -> list[str]:

        signals = []

        for page in pages:

            text = "\n".join(
                page.headings + page.paragraphs
            )

            lower = text.lower()

            for keyword in KEYWORDS:

                if keyword.lower() in lower:
                    signals.append(keyword)

        return sorted(set(signals))