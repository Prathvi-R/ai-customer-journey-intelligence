from app.models.cta import CTA
from app.models.cta import CTACollection
from app.models.website import WebsiteData


class CTAAnalyzer:
    """
    Extracts and categorizes Call-To-Actions
    from every crawled page.
    """

    PRIMARY_KEYWORDS = [
        "enquire",
        "contact",
        "book",
        "call",
        "visit",
        "schedule",
        "buy",
        "register",
        "join",
        "apply",
        "download",
        "get started",
        "request",
    ]

    SECONDARY_KEYWORDS = [
        "know more",
        "learn more",
        "explore",
        "discover",
        "read more",
        "view",
        "see more",
    ]

    @staticmethod
    def analyze(
        website: WebsiteData,
    ) -> CTACollection:

        collection = CTACollection()

        for page in website.pages:

            for button in page.buttons:

                text = button.strip()

                if not text:
                    continue

                lower = text.lower()

                cta_type = "other"
                importance = 0.5

                if any(
                    keyword in lower
                    for keyword in CTAAnalyzer.PRIMARY_KEYWORDS
                ):
                    cta_type = "primary"
                    importance = 1.0

                elif any(
                    keyword in lower
                    for keyword in CTAAnalyzer.SECONDARY_KEYWORDS
                ):
                    cta_type = "secondary"
                    importance = 0.7

                cta = CTA(
                    text=text,
                    page_title=page.title,
                    page_url=page.url,
                    cta_type=cta_type,
                    importance=importance,
                )

                collection.ctas.append(cta)

                if cta_type == "primary":
                    collection.primary_ctas.append(cta)

                elif cta_type == "secondary":
                    collection.secondary_ctas.append(cta)

        return collection