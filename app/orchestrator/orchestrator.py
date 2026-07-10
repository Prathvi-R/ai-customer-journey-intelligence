import asyncio

from app.agents.copy_agent import CopyAgent
from app.agents.journey_agent import JourneyAgent
from app.agents.persona_agent import PersonaAgent
from app.agents.report_agent import ReportAgent
from app.agents.seo_agent import SEOAgent
from app.agents.strategy_agent import StrategyAgent
from app.agents.trust_agent import TrustAgent
from app.agents.ux_agent import UXAgent

from app.models.report import AgentResult


class Orchestrator:

    AGENTS = {

        "PersonaAgent": PersonaAgent,

        "CopyAgent": CopyAgent,

        "SEOAgent": SEOAgent,

        "TrustAgent": TrustAgent,

        "JourneyAgent": JourneyAgent,

        "UXAgent": UXAgent,

        "StrategyAgent": StrategyAgent,

    }

    ##########################################################

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

        question,

    ):

        plan = await self.planner.run(question)

        context = self.retriever.retrieve_context(

            question,

            top_k=10,

        )

        tasks = []

        names = []

        for name in plan.agents:

            agent = self.AGENTS[name](self.llm)

            tasks.append(

                agent.run(

                    question,

                    context,

                )

            )

            names.append(name)

        answers = await asyncio.gather(*tasks)

        reports = []

        for name, answer in zip(names, answers):

            reports.append(

                AgentResult(

                    agent=name,

                    report=answer,

                )

            )

        return await ReportAgent(

            self.llm,

        ).run(

            question,

            reports,

        )