from app.analyzers.contact import ContactAnalyzer
from app.analyzers.journey import JourneyAnalyzer
from app.models.website import WebsiteData


class WebsiteAnalyzer:
    """
    Runs all website-level analyzers and enriches
    WebsiteData with higher-level insights.
    """

    @staticmethod
    def analyze(
        website: WebsiteData,
    ) -> WebsiteData:

        # -----------------------------------------
        # Contact Information
        # -----------------------------------------

        website.contacts = ContactAnalyzer.extract(
            website.pages
        )

        # -----------------------------------------
        # Customer Journey
        # -----------------------------------------

        website.journey = JourneyAnalyzer.analyze(
            website
        )

        # -----------------------------------------
        # Future analyzers
        # -----------------------------------------
        #
        # website.navigation =
        #     NavigationAnalyzer.analyze(website)
        #
        # website.trust_signals =
        #     TrustAnalyzer.analyze(website)
        #
        # website.projects =
        #     ProjectAnalyzer.analyze(website)
        #
        # website.blogs =
        #     BlogAnalyzer.analyze(website)
        #
        # website.personas =
        #     PersonaAnalyzer.analyze(website)
        #
        # website.customer_pain_points =
        #     PainPointAnalyzer.analyze(website)
        #
        # website.funnel =
        #     FunnelAnalyzer.analyze(website)
        #

        return website