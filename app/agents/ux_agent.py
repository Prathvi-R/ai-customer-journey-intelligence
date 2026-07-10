from app.agents.base import BaseAgent
from app.agents.prompts.ux import SYSTEM_PROMPT


class UXAgent(BaseAgent):

    def __init__(self, llm):
        self.llm = llm

    async def run(
        self,
        question: str,
        context: str,
    ):

        prompt = f"""
Website

{context}

Review the UX.

Evaluate:

Navigation

Hierarchy

Readability

Spacing

Information Architecture

CTA placement

Forms

Accessibility

Question

{question}
"""

        return await self.llm.generate(
            SYSTEM_PROMPT,
            prompt,
        )