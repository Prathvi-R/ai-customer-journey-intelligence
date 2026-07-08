from app.agents.base import BaseAgent
from app.agents.prompts import SYSTEM_PROMPT

from app.embeddings.retrieval import Retriever
from app.services.llm import LLMService


class WebsiteAgent(BaseAgent):

    def __init__(
        self,
        retriever: Retriever,
        llm: LLMService,
    ):

        self.retriever = retriever
        self.llm = llm

    #######################################################

    async def run(
        self,
        question: str,
    ) -> str:

        context = self.retriever.retrieve_context(
            query=question,
            top_k=6,
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