from app.intelligence.prompts import PromptFactory
from app.models.website import WebsiteData


class SummaryGenerator:
    """
    Generates executive business summaries
    using an LLM.
    """

    @staticmethod
    def system_prompt() -> str:

        return """
You are an expert business consultant.

Analyze the supplied company information.

Produce:

1. Company Overview
2. Business Model
3. Target Customers
4. Key Offerings
5. Brand Positioning
6. Competitive Strengths

Return clean markdown.
""".strip()

    @staticmethod
    def user_prompt(
        website: WebsiteData,
    ) -> str:

        return PromptFactory.website_context(
            website
        )