from app.models.journey import (
    CustomerJourney,
    JourneyNode,
)
from app.models.website import WebsiteData
from app.models.enums import PageType


class JourneyAnalyzer:
    """
    Builds a simplified customer journey from the
    crawled website.
    """

    @staticmethod
    def analyze(
        website: WebsiteData,
    ) -> CustomerJourney:

        journey = CustomerJourney()

        for page in website.pages:

            node = JourneyNode(
                title=page.title,
                url=page.url,
                page_type=page.page_type.value,
                description=page.description,
            )

            match page.page_type:

                case PageType.HOME:
                    journey.entry_pages.append(node)

                case PageType.ABOUT:
                    journey.trust_pages.append(node)

                case PageType.PROJECT:
                    journey.consideration_pages.append(node)

                case PageType.SERVICE:
                    journey.consideration_pages.append(node)

                case PageType.BLOG:
                    journey.awareness_pages.append(node)

                case PageType.CONTACT:
                    journey.conversion_pages.append(node)

                case PageType.CAREER:
                    journey.support_pages.append(node)

                case _:
                    pass

        return journey