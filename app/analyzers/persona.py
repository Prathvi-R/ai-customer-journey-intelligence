from collections import defaultdict

from app.models.persona import (
    Persona,
    PersonaData,
)
from app.models.website import WebsiteData


class PersonaAnalyzer:
    """
    Infers customer personas
    from website content.
    """

    PERSONA_KEYWORDS = {

        "Luxury Buyers": [
            "luxury",
            "premium",
            "exclusive",
            "elite",
            "high-end",
            "world class",
        ],

        "Families": [
            "family",
            "families",
            "children",
            "kids",
            "community",
            "school",
        ],

        "Investors": [
            "investment",
            "roi",
            "returns",
            "growth",
            "capital",
            "investor",
        ],

        "Home Buyers": [
            "residential",
            "apartment",
            "2 bhk",
            "3 bhk",
            "4 bhk",
            "flat",
            "home",
            "living",
        ],

        "Businesses": [
            "commercial",
            "office",
            "workspace",
            "retail",
            "business",
        ],

        "Students": [
            "student",
            "course",
            "training",
            "education",
            "campus",
        ]
    }

    @staticmethod
    def analyze(
        website: WebsiteData,
    ) -> PersonaData:

        scores = defaultdict(int)

        evidence = defaultdict(list)

        for page in website.pages:

            text = " ".join(
                page.headings +
                page.paragraphs
            ).lower()

            for persona, keywords in (
                PersonaAnalyzer.PERSONA_KEYWORDS.items()
            ):

                for keyword in keywords:

                    if keyword in text:

                        scores[persona] += 1

                        evidence[persona].append(keyword)

        result = PersonaData()

        if not scores:
            return result

        highest = max(scores.values())

        for persona, score in sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True,
        ):

            result.personas.append(

                Persona(

                    name=persona,

                    confidence=round(
                        score / highest,
                        2,
                    ),

                    evidence=sorted(
                        set(evidence[persona])
                    ),
                )

            )

        return result