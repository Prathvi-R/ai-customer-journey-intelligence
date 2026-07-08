from app.agents.base import BaseAgent
from app.agents.prompts.journey import SYSTEM_PROMPT


class JourneyAgent(BaseAgent):

    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm

    async def run(self, question: str):

        context = self.retriever.retrieve_context(question, top_k=8)

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
            SYSTEM_PROMPT,
            prompt,
        )