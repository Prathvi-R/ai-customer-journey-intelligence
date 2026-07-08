from enum import Enum


class AgentType(str, Enum):

    PERSONA = "PersonaAgent"

    JOURNEY = "JourneyAgent"

    UX = "UXAgent"

    TRUST = "TrustAgent"

    COPY = "CopyAgent"

    SEO = "SEOAgent"