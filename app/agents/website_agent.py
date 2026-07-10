from app.agents.base import BaseAgent
from app.agents.prompts import SYSTEM_PROMPT


class WebsiteAgent(BaseAgent):

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

Question

{question}
"""

        return await self.llm.generate(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=prompt,
        )