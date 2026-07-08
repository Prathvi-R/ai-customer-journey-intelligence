from collections import Counter

from app.models.competitor import CompetitorInsight
from app.models.website import WebsiteData


class CompetitorAnalyzer:
    """
    Infers competitive positioning from website content.
    """

    ADVANTAGE_KEYWORDS = [

        "years",
        "legacy",
        "luxury",
        "premium",
        "award",
        "trusted",
        "innovation",
        "quality",
        "experience",
        "community",
        "technology",
        "green",
        "smart",
        "exclusive",

    ]

    MARKET_SEGMENTS = {

        "Luxury": [
            "luxury",
            "premium",
            "exclusive",
            "elite",
        ],

        "Affordable": [
            "affordable",
            "budget",
            "value",
            "economical",
        ],

        "Commercial": [
            "office",
            "commercial",
            "workspace",
        ],

        "Residential": [
            "apartment",
            "home",
            "residential",
            "living",
        ],

        "Mixed Use": [
            "mixed use",
            "township",
            "community",
        ],
    }

    @staticmethod
    def analyze(
        website: WebsiteData,
    ) -> CompetitorInsight:

        insight = CompetitorInsight()

        insight.industry = website.brand.industry

        text = " ".join(

            paragraph

            for page in website.pages

            for paragraph in (
                page.headings +
                page.paragraphs
            )

        ).lower()

        # -------------------------
        # Market Segment
        # -------------------------

        scores = Counter()

        for segment, keywords in (
            CompetitorAnalyzer.MARKET_SEGMENTS.items()
        ):

            for keyword in keywords:

                scores[segment] += text.count(keyword)

        if scores:

            insight.market_segment = scores.most_common(1)[0][0]

        # -------------------------
        # Competitive Advantages
        # -------------------------

        for keyword in CompetitorAnalyzer.ADVANTAGE_KEYWORDS:

            if keyword in text:

                insight.competitive_advantages.append(
                    keyword
                )

        # -------------------------
        # Differentiation Keywords
        # -------------------------

        insight.differentiation_keywords = (

            website.brand.keywords[:15]

        )

        # -------------------------
        # Likely Competitors
        # -------------------------

        # Placeholder until external search
        # or market intelligence is added.

        insight.likely_competitors = []

        return insight