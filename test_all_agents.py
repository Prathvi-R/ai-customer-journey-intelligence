import asyncio

from dotenv import load_dotenv

load_dotenv()

from app.services.storage import StorageService
from app.embeddings.builder import EmbeddingBuilder
from app.embeddings.chroma_store import ChromaStore
from app.embeddings.retrieval import Retriever
from app.services.llm import LLMService
from app.models.llm import TaskType

from app.agents.planner import PlannerAgent
from app.orchestrator.orchestrator import Orchestrator


async def main():

    storage = StorageService()

    website = storage.load_latest_website()

    embedding_data = EmbeddingBuilder.build(website)

    run_dir = storage.latest_directory()

    store = ChromaStore()
    store.build(embedding_data.chunks, run_dir)

    retriever = Retriever(store)

    llm = LLMService.recommended(TaskType.REASONING)

    planner = PlannerAgent(llm)

    orchestrator = Orchestrator(
        planner,
        retriever,
        llm,
    )

    questions = [
        "Who is the ideal customer?",
        "Improve homepage copy.",
        "How can SEO be improved?",
        "Increase trust on homepage.",
        "How should the website grow over the next year?",
        "Why are users leaving the website?"
    ]

    for q in questions:
        print("=" * 80)
        print(f"QUESTION: {q}\n")

        result = await orchestrator.run(q)

        print(result)
        print()


asyncio.run(main())