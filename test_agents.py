import asyncio

from dotenv import load_dotenv

load_dotenv()

from app.services.storage import StorageService
from app.embeddings.builder import EmbeddingBuilder
from app.embeddings.chroma_store import ChromaStore
from app.embeddings.retrieval import Retriever

from app.services.llm import LLMService
from app.models.llm import TaskType

from app.agents.persona_agent import PersonaAgent
from app.agents.copy_agent import CopyAgent
from app.agents.seo_agent import SEOAgent
from app.agents.trust_agent import TrustAgent
from app.agents.ux_agent import UXAgent
from app.agents.journey_agent import JourneyAgent
from app.agents.strategy_agent import StrategyAgent


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

    llm = LLMService.recommended(TaskType.REASONING)

    agents = [

        (
            "Persona",
            PersonaAgent(retriever, llm),
            "Who is the ideal customer?"
        ),

        (
            "SEO",
            SEOAgent(retriever, llm),
            "Audit the SEO."
        ),

        (
            "Copy",
            CopyAgent(retriever, llm),
            "Improve homepage copy."
        ),

        (
            "Trust",
            TrustAgent(retriever, llm),
            "How can trust be improved?"
        ),

        (
            "UX",
            UXAgent(retriever, llm),
            "Review the UX."
        ),

        (
            "Journey",
            JourneyAgent(retriever, llm),
            "Analyze the customer journey."
        ),

        (
            "Strategy",
            StrategyAgent(retriever, llm),
            "Analyze the business strategy."
        ),

    ]

    for name, agent, question in agents:

        print("=" * 80)
        print(name.upper())
        print("=" * 80)

        answer = await agent.run(question)

        print(answer)
        print()


asyncio.run(main())