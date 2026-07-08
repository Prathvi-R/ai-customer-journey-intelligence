from app.models.enums import PageType
from app.models.funnel import FunnelData
from app.models.website import WebsiteData


class FunnelAnalyzer:
    """
    Builds a customer acquisition funnel
    from crawled pages.
    """

    CTA_KEYWORDS = [

        "contact",
        "enquire",
        "enquire now",
        "book",
        "schedule",
        "call",
        "visit",
        "download",
        "buy",
        "register",
        "apply",
        "quote",
        "get started",
        "know more",
    ]

    @staticmethod
    def analyze(
        website: WebsiteData,
    ) -> FunnelData:

        funnel = FunnelData()

        for page in website.pages:

            title = page.title

            buttons = [
                button.lower()
                for button in page.buttons
                if button.strip()
            ]

            actions = []

            for button in buttons:

                for keyword in FunnelAnalyzer.CTA_KEYWORDS:

                    if keyword in button:
                        actions.append(button)

            if page.page_type == PageType.HOME:

                funnel.awareness.pages.append(title)

            elif page.page_type == PageType.BLOG:

                funnel.awareness.pages.append(title)

            elif page.page_type in (

                PageType.PROJECT,
                PageType.PRODUCT,
                PageType.SERVICE,

            ):

                funnel.consideration.pages.append(title)

                funnel.consideration.conversion_actions.extend(
                    actions
                )

            elif page.page_type == PageType.ABOUT:

                funnel.trust.pages.append(title)

            elif page.page_type == PageType.CONTACT:

                funnel.conversion.pages.append(title)

                funnel.conversion.conversion_actions.extend(
                    actions
                )

            elif page.page_type == PageType.CAREER:

                funnel.retention.pages.append(title)

        total_pages = max(
            len(website.pages),
            1,
        )

        for stage in [

            funnel.awareness,
            funnel.consideration,
            funnel.trust,
            funnel.conversion,
            funnel.retention,

        ]:

            stage.conversion_actions = sorted(
                set(stage.conversion_actions)
            )

            stage.confidence = round(
                len(stage.pages) / total_pages,
                2,
            )

        return funnel