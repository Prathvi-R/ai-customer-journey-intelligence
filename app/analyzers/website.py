from app.analyzers.brand import BrandAnalyzer
from app.analyzers.competitor import CompetitorAnalyzer
from app.analyzers.contact import ContactAnalyzer
from app.analyzers.funnel import FunnelAnalyzer
from app.analyzers.journey import JourneyAnalyzer
from app.analyzers.navigation import NavigationAnalyzer
from app.analyzers.pain_points import PainPointAnalyzer
from app.analyzers.persona import PersonaAnalyzer
from app.analyzers.project import ProjectAnalyzer
from app.analyzers.trust import TrustAnalyzer
from app.models.website import WebsiteData


class WebsiteAnalyzer:

    @staticmethod
    def analyze(
        website: WebsiteData,
    ) -> WebsiteData:

        website.contacts = ContactAnalyzer.extract(
            website.pages
        )

        website.journey = JourneyAnalyzer.analyze(
            website
        )

        website.navigation = NavigationAnalyzer.analyze(
            website
        )

        website.trust = TrustAnalyzer.analyze(
            website.pages
        )

        website.projects = ProjectAnalyzer.analyze(
            website.pages
        )

        website.personas = PersonaAnalyzer.analyze(
            website
        )

        website.pain_points = PainPointAnalyzer.analyze(
            website
        )

        website.funnel = FunnelAnalyzer.analyze(
            website
        )

        website.brand = BrandAnalyzer.analyze(
            website
        )

        website.competitors = CompetitorAnalyzer.analyze(
            website
        )

        return website