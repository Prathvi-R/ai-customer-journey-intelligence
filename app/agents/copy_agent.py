from app.agents.base import BaseAgent
from app.agents.prompts.copy import SYSTEM_PROMPT


class CopyAgent(BaseAgent):

    def __init__(
        self,
        retriever,
        llm,
    ):
        self.retriever = retriever
        self.llm = llm

    ###########################################################

    async def run(
        self,
        question: str,
    ):

        context = self.retriever.retrieve_context(
            query=question,
            top_k=8,
        )

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