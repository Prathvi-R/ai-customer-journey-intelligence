import asyncio

from app.agents.persona_agent import PersonaAgent
from app.agents.seo_agent import SEOAgent
from app.agents.ux_agent import UXAgent
from app.agents.copy_agent import CopyAgent
from app.agents.trust_agent import TrustAgent
from app.agents.journey_agent import JourneyAgent

from app.agents.report_agent import ReportAgent


class Orchestrator:

    def __init__(self, planner, retriever, llm):

        self.planner = planner

        self.retriever = retriever

        self.llm = llm

    ##############################################################

    async def run(
        self,
        question: str,
    ):

        plan = await self.planner.plan(question)

        tasks = []

        for name in plan.agents:

            if name == "PersonaAgent":
                tasks.append(
                    PersonaAgent(
                        self.retriever,
                        self.llm,
                    ).run(question)
                )

            elif name == "SEOAgent":
                tasks.append(
                    SEOAgent(
                        self.retriever,
                        self.llm,
                    ).run(question)
                )

            elif name == "UXAgent":
                tasks.append(
                    UXAgent(
                        self.retriever,
                        self.llm,
                    ).run(question)
                )

            elif name == "TrustAgent":
                tasks.append(
                    TrustAgent(
                        self.retriever,
                        self.llm,
                    ).run(question)
                )

            elif name == "JourneyAgent":
                tasks.append(
                    JourneyAgent(
                        self.retriever,
                        self.llm,
                    ).run(question)
                )

            elif name == "CopyAgent":
                tasks.append(
                    CopyAgent(
                        self.retriever,
                        self.llm,
                    ).run(question)
                )

        outputs = await asyncio.gather(*tasks)

        report = ReportAgent(
            self.llm
        )

        return await report.run(
            question,
            outputs,
        )