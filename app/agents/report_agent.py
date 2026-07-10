from app.agents.prompts.report import SYSTEM_PROMPT


class ReportAgent:

    def __init__(self, llm):

        self.llm = llm

    ##########################################################

    async def run(
        self,
        question,
        reports,
    ):

        sections = []

        for result in reports:

            sections.append(

                f"""
# {result.agent}

{result.report}
"""

            )

        joined = "\n\n".join(sections)

        prompt = f"""
User Question

{question}

Specialist Reports

{joined}

Create ONE final consulting report.

Requirements

- Merge overlapping findings
- Remove duplicates
- Prioritize highest-impact issues
- Use markdown headings
- Produce an executive summary
- End with an action plan
"""

        return await self.llm.generate(
            SYSTEM_PROMPT,
            prompt,
        )