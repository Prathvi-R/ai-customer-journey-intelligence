from app.intelligence.prompts import PromptFactory
from app.models.website import WebsiteData


class OpportunityGenerator:
    """
    Finds growth opportunities.
    """

    @staticmethod
    def system_prompt() -> str:

        return """
You are a startup advisor.

Find opportunities in:

- Revenue
- Marketing
- Automation
- AI
- Sales
- Customer Experience

Rank each:

High

Medium

Low

Return markdown.
""".strip()

    @staticmethod
    def user_prompt(
        website: WebsiteData,
    ) -> str:

        return PromptFactory.website_context(
            website
        )