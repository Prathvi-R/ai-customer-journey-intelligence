from collections import Counter

from app.models.brand import BrandData
from app.models.website import WebsiteData


class BrandAnalyzer:
    """
    Infers high-level brand identity
    from website content.
    """

    INDUSTRIES = {

        "Real Estate": [
            "apartment",
            "residential",
            "commercial",
            "project",
            "builder",
            "construction",
            "property",
            "homes",
        ],

        "Healthcare": [
            "hospital",
            "doctor",
            "clinic",
            "patient",
            "medical",
        ],

        "Education": [
            "school",
            "college",
            "course",
            "student",
            "training",
        ],

        "Technology": [
            "software",
            "platform",
            "cloud",
            "ai",
            "technology",
            "saas",
        ],

        "Finance": [
            "bank",
            "insurance",
            "investment",
            "loan",
            "finance",
        ],
    }

    POSITIONING = {

        "Luxury": [
            "luxury",
            "premium",
            "exclusive",
            "elite",
        ],

        "Affordable": [
            "budget",
            "affordable",
            "value",
            "price",
            "cost",
        ],

        "Modern": [
            "modern",
            "innovation",
            "future",
            "smart",
        ],

        "Sustainable": [
            "green",
            "eco",
            "nature",
            "environment",
        ],
    }

    TONES = {

        "Professional": [
            "experience",
            "legacy",
            "trusted",
            "years",
        ],

        "Friendly": [
            "community",
            "family",
            "together",
            "welcome",
        ],

        "Luxury": [
            "luxury",
            "premium",
            "exclusive",
        ],

        "Innovative": [
            "innovation",
            "technology",
            "future",
        ],
    }

    @staticmethod
    def analyze(
        website: WebsiteData,
    ) -> BrandData:

        brand = BrandData()

        text = " ".join(

            heading

            for page in website.pages

            for heading in (
                page.headings +
                page.paragraphs
            )

        ).lower()

        # ------------------------
        # Industry
        # ------------------------

        industry_scores = Counter()

        for industry, keywords in (
            BrandAnalyzer.INDUSTRIES.items()
        ):

            for keyword in keywords:

                industry_scores[industry] += text.count(
                    keyword
                )

        if industry_scores:

            brand.industry = industry_scores.most_common(1)[0][0]

        # ------------------------
        # Positioning
        # ------------------------

        position_scores = Counter()

        for position, keywords in (
            BrandAnalyzer.POSITIONING.items()
        ):

            for keyword in keywords:

                position_scores[position] += text.count(
                    keyword
                )

        if position_scores:

            brand.positioning = position_scores.most_common(1)[0][0]

        # ------------------------
        # Tone
        # ------------------------

        tone_scores = Counter()

        for tone, keywords in (
            BrandAnalyzer.TONES.items()
        ):

            for keyword in keywords:

                tone_scores[tone] += text.count(
                    keyword
                )

        if tone_scores:

            brand.tone = tone_scores.most_common(1)[0][0]

        # ------------------------
        # Value Propositions
        # ------------------------

        for page in website.pages:

            for heading in page.headings[:5]:

                if len(heading) > 12:

                    brand.value_propositions.append(
                        heading
                    )

        brand.value_propositions = list(

            dict.fromkeys(

                brand.value_propositions

            )

        )[:8]

        # ------------------------
        # Mission
        # ------------------------

        for page in website.pages:

            if page.paragraphs:

                paragraph = page.paragraphs[0]

                if len(paragraph) > 30:

                    brand.mission = paragraph

                    break

        # ------------------------
        # Differentiators
        # ------------------------

        differentiator_words = [

            "legacy",
            "experience",
            "premium",
            "luxury",
            "innovation",
            "quality",
            "community",
            "award",
            "trusted",
        ]

        found = []

        for word in differentiator_words:

            if word in text:

                found.append(word)

        brand.differentiators = found

        # ------------------------
        # Keywords
        # ------------------------

        keywords = Counter()

        for page in website.pages:

            for heading in page.headings:

                for word in heading.lower().split():

                    if len(word) >= 5:

                        keywords[word] += 1

        brand.keywords = [

            word

            for word, _ in keywords.most_common(20)

        ]

        return brand