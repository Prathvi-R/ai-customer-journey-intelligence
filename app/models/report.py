from pydantic import BaseModel, Field


class AgentResult(BaseModel):

    agent: str

    report: str


class FinalReport(BaseModel):

    question: str

    reports: list[AgentResult] = Field(default_factory=list)

    final_answer: str