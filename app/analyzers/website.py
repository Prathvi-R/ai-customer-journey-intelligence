from app.analyzers.contact import ContactAnalyzer
from app.analyzers.journey import JourneyAnalyzer
from app.analyzers.navigation import NavigationAnalyzer
from app.models import website
from app.models.website import WebsiteData
from app.analyzers.cta import CTAAnalyzer


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
        # Navigation Graph
        # -----------------------------------------

        website.navigation = NavigationAnalyzer.analyze(
            website
        )

        # -----------------------------------------
        # CTA Analysis
        # -----------------------------------------

        website.cta = CTAAnalyzer.analyze(
            website
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
        # website.seo =
        #     SEOAnalyzer.analyze(website)
        #
        # website.content =
        #     ContentAnalyzer.analyze(website)
        #

        return website