from app.agents.base import BaseAgent
from app.agents.prompts.strategy import SYSTEM_PROMPT


class StrategyAgent(BaseAgent):

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

Act as a Product Strategy Consultant.

Evaluate:

Business positioning

Competitive differentiation

ICP

Messaging

Growth opportunities

Pricing communication

Trust

Question

{question}
"""

        return await self.llm.generate(
            SYSTEM_PROMPT,
            prompt,
        )