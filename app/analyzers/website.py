from app.analyzers.navigation import NavigationAnalyzer
from app.analyzers.projects import ProjectsAnalyzer
from app.analyzers.trust import TrustAnalyzer
from app.analyzers.contact import ContactAnalyzer
from app.models.website import WebsiteData


class WebsiteAnalyzer:
    """
    Runs all website-level analyzers.
    """

    @staticmethod
    def analyze(website: WebsiteData) -> WebsiteData:

        website.navigation = NavigationAnalyzer.extract(
            website.pages
        )

        website.projects = ProjectsAnalyzer.extract(
            website.pages
        )

        website.trust_signals = TrustAnalyzer.extract(
            website.pages
        )

        website.contacts = ContactAnalyzer.extract(
            website.pages
        )

        return website