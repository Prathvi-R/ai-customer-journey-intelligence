from app.analyzers.brand import BrandAnalyzer
from app.analyzers.competitor import CompetitorAnalyzer
from app.analyzers.contact import ContactAnalyzer
from app.analyzers.cta import CTAAnalyzer
from app.analyzers.funnel import FunnelAnalyzer
from app.analyzers.journey import JourneyAnalyzer
from app.analyzers.navigation import NavigationAnalyzer
from app.analyzers.pain_point import PainPointAnalyzer
from app.analyzers.persona import PersonaAnalyzer
from app.analyzers.project import ProjectAnalyzer
from app.analyzers.trust import TrustAnalyzer

from app.embeddings.builder import EmbeddingBuilder
from app.knowledge.builder import KnowledgeGraphBuilder

from app.models.website import WebsiteData


class WebsiteAnalyzer:
    """
    Runs every website-level analyzer and enriches
    WebsiteData with higher-level intelligence.
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
        # Navigation
        # -----------------------------------------

        website.navigation = NavigationAnalyzer.analyze(
            website
        )

        # -----------------------------------------
        # Trust Signals
        # -----------------------------------------

        website.trust = TrustAnalyzer.analyze(
            website.pages
        )

        # -----------------------------------------
        # Projects / Products / Services
        # -----------------------------------------

        website.projects = ProjectAnalyzer.analyze(
            website.pages
        )

        # -----------------------------------------
        # Personas
        # -----------------------------------------

        website.personas = PersonaAnalyzer.analyze(
            website
        )

        # -----------------------------------------
        # Customer Pain Points
        # -----------------------------------------

        website.pain_points = PainPointAnalyzer.analyze(
            website
        )

        # -----------------------------------------
        # Brand
        # -----------------------------------------

        website.brand = BrandAnalyzer.analyze(
            website
        )

        # -----------------------------------------
        # Calls-to-Action
        # -----------------------------------------

        website.ctas = CTAAnalyzer.analyze(
            website
        )

        # -----------------------------------------
        # Competitors
        # -----------------------------------------

        website.competitors = CompetitorAnalyzer.analyze(
            website
        )

        # -----------------------------------------
        # Customer Funnel
        # -----------------------------------------

        website.funnel = FunnelAnalyzer.analyze(
            website
        )

        # -----------------------------------------
        # Knowledge Graph
        # -----------------------------------------

        website.knowledge_graph = (
            KnowledgeGraphBuilder.build(
                website
            )
        )

        # -----------------------------------------
        # Embedding Chunks
        # -----------------------------------------

        website.embeddings = (
            EmbeddingBuilder.build(
                website
            )
        )

        return website