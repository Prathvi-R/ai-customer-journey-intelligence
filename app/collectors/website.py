from app.collectors.crawl_state import CrawlState
from app.models.crawl import CrawlResult
from app.models.website import WebsiteData
from app.services.browser import BrowserService
from app.services.extractor import ExtractionService
from app.services.url import URLService
from app.utils.logger import logger


class WebsiteCollector:
    """
    Breadth-First Search (BFS) website collector.

    Responsibilities:
    - Crawl internal pages
    - Extract structured page data
    - Build WebsiteData
    """

    def __init__(
        self,
        base_url: str,
        max_pages: int = 25,
        headless: bool = True,
    ):
        self.base_url = URLService.normalize(base_url)

        self.max_pages = max_pages

        self.browser = BrowserService(headless=headless)

        self.state = CrawlState(self.base_url)

    async def collect(self) -> CrawlResult:

        logger.info(f"Starting crawl: {self.base_url}")

        await self.browser.start()

        website = WebsiteData(
            base_url=self.base_url,
        )

        try:

            while (
                self.state.has_next()
                and len(self.state.visited) < self.max_pages
            ):

                current_url = self.state.next_url()

                if current_url in self.state.visited:
                    continue

                logger.info(f"Crawling: {current_url}")

                try:

                    page = await self.browser.new_page()

                    await self.browser.goto(
                        page,
                        current_url,
                    )

                    page_data = await ExtractionService.extract(page)

                    website.pages.append(page_data)

                    self.state.mark_visited(current_url)

                    logger.info(
                        f"Extracted {len(page_data.links)} links from {current_url}"
                    )

                    for href in page_data.links:

                        if not URLService.is_crawlable(href):
                            continue

                        absolute = URLService.absolute(
                            current_url,
                            href,
                        )

                        normalized = URLService.normalize(
                            absolute,
                        )

                        if not URLService.is_internal(
                            self.base_url,
                            normalized,
                        ):
                            continue

                        self.state.enqueue(normalized)

                    await page.close()

                except Exception as e:

                    logger.exception(
                        f"Failed to crawl {current_url}: {e}"
                    )

                    self.state.mark_failed(current_url)

            logger.success(
                f"Crawl completed. "
                f"Visited={len(self.state.visited)}, "
                f"Failed={len(self.state.failed)}"
            )

            return CrawlResult(
                visited_urls=sorted(self.state.visited),
                failed_urls=self.state.failed,
                website_data=website,
            )

        finally:

            await self.browser.close()