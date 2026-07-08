import asyncio

from dotenv import load_dotenv

load_dotenv()

from app.models.llm import TaskType
from app.services.llm import LLMService

from app.agents.planner import PlannerAgent


async def main():

    llm = LLMService.recommended(
        TaskType.CHEAP
    )

    planner = PlannerAgent(
        llm
    )

    questions = [

        "Who is the ideal customer?",

        "Improve homepage copy.",

        "Why are users leaving the website?",

        "How can SEO be improved?",

        "Increase trust on homepage."

    ]

    for q in questions:

        print("=" * 50)

        print(q)

        result = await planner.run(
            q
        )

        print(result.model_dump())


asyncio.run(main())