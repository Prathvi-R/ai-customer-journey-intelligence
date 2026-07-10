import asyncio

from app.agents.copy_agent import CopyAgent
from app.agents.journey_agent import JourneyAgent
from app.agents.persona_agent import PersonaAgent
from app.agents.report_agent import ReportAgent
from app.agents.seo_agent import SEOAgent
from app.agents.strategy_agent import StrategyAgent
from app.agents.trust_agent import TrustAgent
from app.agents.ux_agent import UXAgent


class Orchestrator:

    AGENT_REGISTRY = {
        "PersonaAgent": PersonaAgent,
        "CopyAgent": CopyAgent,
        "SEOAgent": SEOAgent,
        "TrustAgent": TrustAgent,
        "JourneyAgent": JourneyAgent,
        "UXAgent": UXAgent,
        "StrategyAgent": StrategyAgent,
    }

    ############################################################

    def __init__(
        self,
        planner,
        retriever,
        llm,
    ):

        self.planner = planner
        self.retriever = retriever
        self.llm = llm

    ############################################################

    async def run(
        self,
        question: str,
    ):

        # Step 1: Planner chooses agents

        plan = await self.planner.run(question)

        # Step 2: Retrieve context ONCE

        context = self.retriever.retrieve_context(
            query=question,
            top_k=8,
        )

        # Step 3: Run selected agents

        tasks = []

        for agent_name in plan.agents:

            agent_cls = self.AGENT_REGISTRY.get(agent_name)

            if agent_cls is None:
                print(f"Unknown agent: {agent_name}")
                continue

            agent = agent_cls(self.llm)

            tasks.append(
                agent.run(
                    question,
                    context,
                )
            )

        outputs = await asyncio.gather(*tasks)

        # Step 4: Merge results

        report_agent = ReportAgent(self.llm)

        return await report_agent.run(
            question,
            outputs,
        )