import asyncio

from dotenv import load_dotenv

load_dotenv()

from app.embeddings.builder import EmbeddingBuilder
from app.embeddings.chroma_store import ChromaStore
from app.embeddings.retrieval import Retriever

from app.models.llm import TaskType
from app.services.llm import LLMService
from app.services.storage import StorageService

from app.agents.website_agent import WebsiteAgent


async def main():

    storage = StorageService()

    website = storage.load_latest_website()

    embedding_data = EmbeddingBuilder.build(
        website
    )

    run_dir = storage.latest_directory()

    store = ChromaStore()

    store.build(
        embedding_data.chunks,
        run_dir,
    )

    retriever = Retriever(
        store
    )

    llm = LLMService.recommended(
        TaskType.REASONING
    )

    agent = WebsiteAgent(
        retriever,
        llm,
    )

    answer = await agent.run(
        "Who is the ideal customer?"
    )

    print("\nAnswer:\n")
    print(answer)


asyncio.run(main())