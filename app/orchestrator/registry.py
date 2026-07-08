from app.agents.copy_agent import CopyAgent
from app.agents.journey_agent import JourneyAgent
from app.agents.persona_agent import PersonaAgent
from app.agents.seo_agent import SEOAgent
from app.agents.strategy_agent import StrategyAgent
from app.agents.trust_agent import TrustAgent
from app.agents.ux_agent import UXAgent


AGENT_REGISTRY = {

    "PersonaAgent": PersonaAgent,

    "CopyAgent": CopyAgent,

    "SEOAgent": SEOAgent,

    "TrustAgent": TrustAgent,

    "JourneyAgent": JourneyAgent,

    "UXAgent": UXAgent,

    "StrategyAgent": StrategyAgent,

}