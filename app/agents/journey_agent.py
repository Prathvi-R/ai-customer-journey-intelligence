from app.agents.base import BaseAgent
from app.agents.prompts.journey import SYSTEM_PROMPT


class JourneyAgent(BaseAgent):

    def __init__(self, llm):
        self.llm = llm

    async def run(
        self,
        question: str,
        context: str,
    ):

        prompt = f"""
Website Context

{context}

Task

Analyze the complete customer journey.

Identify:

- Landing experience
- Navigation
- Decision points
- Friction
- Drop-offs
- Missing information
- CTA quality

Question

{question}
"""

        return await self.llm.generate(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=prompt,
        )