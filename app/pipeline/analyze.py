from app.embeddings.builder import EmbeddingBuilder
from app.embeddings.chroma_store import ChromaStore
from app.embeddings.retrieval import Retriever

from app.models.llm import TaskType
from app.services.llm import LLMService
from app.services.report import ReportService
from app.services.storage import StorageService

from app.agents.planner import PlannerAgent
from app.orchestrator.orchestrator import Orchestrator


class AnalysisPipeline:

    def __init__(self):

        self.storage = StorageService()

    ###########################################################

    async def run(

        self,

        questions: list[str],

    ):

        website = self.storage.load_latest_website()

        embedding_data = EmbeddingBuilder.build(
            website
        )

        crawl_dir = self.storage.latest_directory()

        store = ChromaStore()

        store.build(
            embedding_data.chunks,
            crawl_dir,
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

        analysis_dir = self.storage.create_run(
            "analysis"
        )

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

        print()

        print("=" * 80)
        print("Analysis Complete")
        print(analysis_dir)