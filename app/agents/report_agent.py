from app.agents.prompts.report import SYSTEM_PROMPT


class ReportAgent:

    def __init__(self, llm):

        self.llm = llm

    async def run(
        self,
        question,
        outputs,
    ):

        joined = "\n\n".join(outputs)

        prompt = f"""
User Question

{question}

Agent Reports

{joined}

Create one unified report.

Do not repeat information.

Group similar findings.

Prioritize highest-impact recommendations.

Return markdown.
"""

        return await self.llm.generate(
            SYSTEM_PROMPT,
            prompt,
        )