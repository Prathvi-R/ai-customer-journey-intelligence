from collections import defaultdict

from app.models.pain_point import (
    PainPoint,
    PainPointData,
)
from app.models.website import WebsiteData


class PainPointAnalyzer:
    """
    Infers customer pain points
    from website content.
    """

    PAIN_POINT_KEYWORDS = {

        "Affordability": [
            "affordable",
            "price",
            "pricing",
            "budget",
            "cost",
            "emi",
            "loan",
        ],

        "Luxury Living": [
            "luxury",
            "premium",
            "exclusive",
            "elite",
            "high-end",
        ],

        "Trust": [
            "legacy",
            "experience",
            "trusted",
            "years",
            "delivered",
            "families",
        ],

        "Location": [
            "location",
            "connectivity",
            "metro",
            "airport",
            "nearby",
        ],

        "Space": [
            "spacious",
            "large",
            "open",
            "layout",
            "floor plan",
        ],

        "Sustainability": [
            "green",
            "eco",
            "nature",
            "environment",
            "sustainable",
        ],

        "Safety": [
            "security",
            "safe",
            "surveillance",
            "cctv",
            "gated",
        ],

        "Health & Wellness": [
            "gym",
            "fitness",
            "wellness",
            "health",
            "garden",
            "park",
        ]
    }

    @staticmethod
    def analyze(
        website: WebsiteData,
    ) -> PainPointData:

        scores = defaultdict(int)

        evidence = defaultdict(list)

        for page in website.pages:

            text = " ".join(
                page.headings +
                page.paragraphs
            ).lower()

            for pain_point, keywords in (
                PainPointAnalyzer.PAIN_POINT_KEYWORDS.items()
            ):

                for keyword in keywords:

                    if keyword in text:

                        scores[pain_point] += 1

                        evidence[pain_point].append(keyword)

        result = PainPointData()

        if not scores:
            return result

        highest = max(scores.values())

        for pain_point, score in sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True,
        ):

            result.pain_points.append(

                PainPoint(

                    name=pain_point,

                    confidence=round(
                        score / highest,
                        2,
                    ),

                    evidence=sorted(
                        set(evidence[pain_point])
                    ),
                )

            )

        return result