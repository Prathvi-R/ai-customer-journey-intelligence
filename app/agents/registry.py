from app.agents.persona_agent import PersonaAgent
from app.agents.journey_agent import JourneyAgent
from app.agents.ux_agent import UXAgent
from app.agents.strategy_agent import StrategyAgent
from app.agents.seo_agent import SEOAgent
from app.agents.copy_agent import CopyAgent
from app.agents.trust_agent import TrustAgent
from app.agents.report_agent import ReportAgent


class AgentRegistry:

    REGISTRY = {

        "PersonaAgent": PersonaAgent,

        "JourneyAgent": JourneyAgent,

        "UXAgent": UXAgent,

        "StrategyAgent": StrategyAgent,

        "SEOAgent": SEOAgent,

        "CopyAgent": CopyAgent,

        "TrustAgent": TrustAgent,

        "ReportAgent": ReportAgent,

    }

    @classmethod
    def get(cls, name):

        if name not in cls.REGISTRY:
            raise ValueError(f"Unknown agent: {name}")

        return cls.REGISTRY[name]