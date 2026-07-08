import json

from app.agents.base import BaseAgent
from app.agents.prompts.planner import SYSTEM_PROMPT

from app.models.planner import PlannerResponse

from app.services.llm import LLMService


class PlannerAgent(BaseAgent):

    def __init__(
        self,
        llm: LLMService,
    ):

        self.llm = llm

    #######################################################

    async def run(
        self,
        question: str,
    ) -> PlannerResponse:

        response = await self.llm.generate(

            system_prompt=SYSTEM_PROMPT,

            user_prompt=question,

        )

        response = response.strip()

        if response.startswith("```"):

            response = (
                response
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

        data = json.loads(response)

        return PlannerResponse(
            **data
        )