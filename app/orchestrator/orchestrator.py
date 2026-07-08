import asyncio

from app.agents.report_agent import ReportAgent
from app.orchestrator.registry import AGENT_REGISTRY


class Orchestrator:

    def __init__(
        self,
        planner,
        retriever,
        llm,
    ):

        self.planner = planner
        self.retriever = retriever
        self.llm = llm

    ##########################################################

    async def run(
        self,
        question: str,
    ):

        # Decide which agents should run
        plan = await self.planner.run(question)

        tasks = []

        for agent_name in plan.agents:

            agent_class = AGENT_REGISTRY.get(agent_name)

            if agent_class is None:

                print(f"Unknown agent: {agent_name}")

                continue

            agent = agent_class(

                self.retriever,

                self.llm,

            )

            tasks.append(

                agent.run(question)

            )

        outputs = await asyncio.gather(*tasks)

        report = await ReportAgent(

            self.llm

        ).run(

            question,

            outputs,

        )

        return report