from app.agents.base import BaseAgent
from app.agents.prompts.ux import SYSTEM_PROMPT


class UXAgent(BaseAgent):

    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm

    async def run(self, question):

        context = self.retriever.retrieve_context(
            question,
            top_k=8,
        )

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