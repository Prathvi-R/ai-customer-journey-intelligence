import asyncio

from dotenv import load_dotenv

load_dotenv()

from app.services.storage import StorageService

from app.embeddings.builder import EmbeddingBuilder
from app.embeddings.chroma_store import ChromaStore
from app.embeddings.retrieval import Retriever

from app.models.llm import TaskType
from app.services.llm import LLMService

from app.agents.planner import PlannerAgent
from app.orchestrator.orchestrator import Orchestrator

from app.services.report import ReportService


async def main():
    
    storage = StorageService()

    ##########################################################
    # Load latest crawl
    ##########################################################

    website = storage.load_latest_website()

    ##########################################################
    # Build embeddings
    ##########################################################

    embedding_data = EmbeddingBuilder.build(
        website
    )

    ##########################################################
    # Load existing crawl directory
    ##########################################################

    crawl_dir = storage.latest_directory()

    store = ChromaStore()

    store.build(
        embedding_data.chunks,
        crawl_dir,
    )

    retriever = Retriever(store)

    ##########################################################
    # LLM
    ##########################################################

    llm = LLMService.recommended(
        TaskType.REASONING
    )

    planner = PlannerAgent(llm)

    orchestrator = Orchestrator(
        planner,
        retriever,
        llm,
    )

    ##########################################################
    # Questions
    ##########################################################

    questions = [

        "Who is the ideal customer?",

        "Improve homepage copy.",

        "How can SEO be improved?",

        "Increase trust on homepage.",

        "How should the website grow over the next year?",

        "Why are users leaving the website?",

    ]

    ##########################################################
    # Create NEW analysis folder
    ##########################################################

    analysis_dir = storage.create_run(
        source="analysis"
    )

    ##########################################################
    # Run agents
    ##########################################################

    for i, question in enumerate(
        questions,
        start=1,
    ):

        print("=" * 80)
        print(question)
        print()

        report = await orchestrator.run(
            question
        )

        print(report)

        filename = f"{i:02d}_{question}"

        ReportService.save_markdown(
            report,
            analysis_dir,
            filename,
        )

        ReportService.save_html(
            report,
            analysis_dir,
            filename,
        )

        ReportService.save_pdf(
            report,
            analysis_dir,
            filename,
        )

        print(
            f"\n✓ Finished Report {i}\n"
        )


if __name__ == "__main__":
    asyncio.run(main())