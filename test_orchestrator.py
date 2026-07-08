import asyncio

from dotenv import load_dotenv

load_dotenv()

from app.services.storage import StorageService
from app.embeddings.builder import EmbeddingBuilder
from app.embeddings.chroma_store import ChromaStore
from app.embeddings.retrieval import Retriever

from app.agents.planner import PlannerAgent
from app.agents.orchestrator import Orchestrator

from app.models.llm import TaskType
from app.services.llm import LLMService


async def main():

    storage = StorageService()

    website = storage.load_latest_website()

    embedding_data = EmbeddingBuilder.build(website)

    run_dir = storage.latest_directory()

    store = ChromaStore()

    store.build(
        embedding_data.chunks,
        run_dir,
    )

    retriever = Retriever(store)

    llm = LLMService.recommended(
        TaskType.REASONING
    )

    planner = PlannerAgent(llm)

    orchestrator = Orchestrator(
        planner,
        retriever,
        llm,
    )

    report = await orchestrator.run(
        "How can Shrreeji Sharan increase conversions on the homepage?"
    )

    print(report)


asyncio.run(main())