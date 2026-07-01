from app.collectors.website import WebsiteCollector
from app.models.crawl import CrawlResult
from app.services.storage import StorageService
from app.utils.logger import logger


class WebsitePipeline:
    """
    Orchestrates website collection.

    Collector
        ↓
    Storage
        ↓
    (Future)
        Embeddings
        Knowledge Graph
        AI Agents
    """

    def __init__(
        self,
        base_url: str,
        max_pages: int = 25,
    ):

        self.collector = WebsiteCollector(
            base_url=base_url,
            max_pages=max_pages,
        )

        self.storage = StorageService()

    async def run(self) -> CrawlResult:

        logger.info("Starting Website Pipeline")

        crawl_result = await self.collector.collect()

        run_directory = self.storage.create_run(
            "website"
        )

        self.storage.save_crawl(
            crawl_result,
            run_directory,
        )

        self.storage.save_website(
            crawl_result.website_data,
            run_directory,
        )

        self.storage.save_pages(
            crawl_result.website_data,
            run_directory,
        )

        logger.success("Pipeline completed.")

        return crawl_result