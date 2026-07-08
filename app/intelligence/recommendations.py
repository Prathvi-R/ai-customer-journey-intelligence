from app.intelligence.prompts import PromptFactory
from app.models.website import WebsiteData


class RecommendationGenerator:
    """
    Produces actionable recommendations.
    """

    @staticmethod
    def system_prompt() -> str:

        return """
You are a Product Manager,
Growth Consultant,
UX Consultant,
SEO Expert,
and CRO Specialist.

Generate prioritized recommendations.

Categories:

- Website
- UX
- Conversion
- SEO
- Branding
- Trust
- AI Automation

Respond using markdown headings.
""".strip()

    @staticmethod
    def user_prompt(
        website: WebsiteData,
    ) -> str:

        return PromptFactory.website_context(
            website
        )