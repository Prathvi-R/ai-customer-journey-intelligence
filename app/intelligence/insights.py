from app.intelligence.prompts import PromptFactory
from app.models.website import WebsiteData


class InsightGenerator:
    """
    Produces strategic insights.
    """

    @staticmethod
    def system_prompt() -> str:

        return """
You are a senior strategy consultant.

Identify:

- Business strengths
- Weaknesses
- Missing information
- Trust gaps
- UX concerns
- Customer concerns
- Opportunities

Respond in markdown.
""".strip()

    @staticmethod
    def user_prompt(
        website: WebsiteData,
    ) -> str:

        return PromptFactory.website_context(
            website
        )