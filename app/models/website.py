from pydantic import Field

from app.models.base import BaseData
from app.models.brand import BrandData
from app.models.competitor import CompetitorInsight
from app.models.contact import ContactData
from app.models.funnel import FunnelData
from app.models.journey import CustomerJourney
from app.models.navigation import NavigationGraph
from app.models.page import PageData
from app.models.pain_points import PainPointData
from app.models.persona import PersonaData
from app.models.project import ProjectCatalog
from app.models.trust import TrustData


class WebsiteData(BaseData):

    base_url: str

    domain: str

    pages: list[PageData] = Field(default_factory=list)

    contacts: ContactData = Field(default_factory=ContactData)

    journey: CustomerJourney = Field(default_factory=CustomerJourney)

    navigation: NavigationGraph = Field(default_factory=NavigationGraph)

    trust: TrustData = Field(default_factory=TrustData)

    projects: ProjectCatalog = Field(default_factory=ProjectCatalog)

    personas: PersonaData = Field(default_factory=PersonaData)

    pain_points: PainPointData = Field(default_factory=PainPointData)

    funnel: FunnelData = Field(default_factory=FunnelData)

    brand: BrandData = Field(default_factory=BrandData)

    competitors: CompetitorInsight = Field(
        default_factory=CompetitorInsight
    )