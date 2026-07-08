from pydantic import Field

from app.models.base import BaseData
from app.models.brand import BrandData
from app.models.competitor import CompetitorData
from app.models.contact import ContactData
from app.models.embedding import EmbeddingData
from app.models.funnel import FunnelData
from app.models.graph import KnowledgeGraph
from app.models.journey import CustomerJourney
from app.models.navigation import NavigationGraph
from app.models.page import PageData
from app.models.pain_point import PainPointData
from app.models.persona import PersonaData
from app.models.project import ProjectCatalog
from app.models.trust import TrustData
from app.models.cta import CTACollection


class WebsiteData(BaseData):
    """
    Complete structured representation of a website.
    """

    # -----------------------------------------
    # Identity
    # -----------------------------------------

    base_url: str

    domain: str

    pages: list[PageData] = Field(
        default_factory=list
    )

    # -----------------------------------------
    # Website Intelligence
    # -----------------------------------------

    contacts: ContactData = Field(
        default_factory=ContactData
    )

    navigation: NavigationGraph = Field(
        default_factory=NavigationGraph
    )

    journey: CustomerJourney = Field(
        default_factory=CustomerJourney
    )

    trust: TrustData = Field(
        default_factory=TrustData
    )

    projects: ProjectCatalog = Field(
        default_factory=ProjectCatalog
    )

    personas: PersonaData = Field(
        default_factory=PersonaData
    )

    pain_points: PainPointData = Field(
        default_factory=PainPointData
    )

    funnel: FunnelData = Field(
        default_factory=FunnelData
    )

    brand: BrandData = Field(
        default_factory=BrandData
    )

    competitors: CompetitorData = Field(
        default_factory=CompetitorData
    )

    ctas: CTACollection = Field(
        default_factory=CTACollection
    )

    # -----------------------------------------
    # AI Layer
    # -----------------------------------------

    knowledge_graph: KnowledgeGraph = Field(
        default_factory=KnowledgeGraph
    )

    embeddings: EmbeddingData = Field(
        default_factory=EmbeddingData
    )