from __future__ import annotations

from datetime import datetime
from pathlib import Path

from app.models.crawl import CrawlResult
from app.models.page import PageData
from app.models.website import WebsiteData
from app.utils.logger import logger


class StorageService:
    """
    Handles persistence of crawl results.

    Responsibilities
    ----------------
    • Create versioned crawl directories
    • Save CrawlResult
    • Save WebsiteData
    • Save individual pages
    • Load previous runs
    • List crawl history
    """

    def __init__(
        self,
        root_directory: str = "data",
    ):

        self.root = Path(root_directory)

    ############################################################
    # CREATE
    ############################################################

    def create_run(
        self,
        source: str = "website",
    ) -> Path:

        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        run_directory = (
            self.root
            / source
            / timestamp
        )

        (run_directory / "pages").mkdir(
            parents=True,
            exist_ok=True,
        )

        (run_directory / "screenshots").mkdir(
            parents=True,
            exist_ok=True,
        )

        logger.info(
            f"Created crawl directory: {run_directory}"
        )

        return run_directory

    ############################################################
    # SAVE
    ############################################################

    def save_crawl(
        self,
        crawl: CrawlResult,
        run_directory: Path,
    ) -> None:

        filepath = (
            run_directory
            / "crawl.json"
        )

        filepath.write_text(
            crawl.model_dump_json(indent=4),
            encoding="utf-8",
        )

        logger.success(
            f"Saved {filepath}"
        )

    ############################################################

    def save_website(
        self,
        website: WebsiteData,
        run_directory: Path,
    ) -> None:

        filepath = (
            run_directory
            / "website.json"
        )

        filepath.write_text(
            website.model_dump_json(indent=4),
            encoding="utf-8",
        )

        logger.success(
            f"Saved {filepath}"
        )

    ############################################################

    def save_page(
        self,
        page: PageData,
        run_directory: Path,
    ):

        slug = (
            page.url
            .replace("https://", "")
            .replace("http://", "")
            .replace("/", "_")
            .replace("?", "_")
            .replace("&", "_")
            .replace("=", "_")
        )

        filepath = (
            run_directory
            / "pages"
            / f"{slug}.json"
        )

        filepath.write_text(
            page.model_dump_json(indent=4),
            encoding="utf-8",
        )

    ############################################################

    def save_pages(
        self,
        website: WebsiteData,
        run_directory: Path,
    ):

        for page in website.pages:
            self.save_page(
                page,
                run_directory,
            )

        logger.success(
            f"Saved {len(website.pages)} pages"
        )

    ############################################################
    # LOAD
    ############################################################

    def load_crawl(
        self,
        run_directory: Path,
    ) -> CrawlResult:

        filepath = (
            run_directory
            / "crawl.json"
        )

        return CrawlResult.model_validate_json(
            filepath.read_text(
                encoding="utf-8",
            )
        )

    ############################################################

    def load_website(
        self,
        run_directory: Path,
    ) -> WebsiteData:

        filepath = (
            run_directory
            / "website.json"
        )

        return WebsiteData.model_validate_json(
            filepath.read_text(
                encoding="utf-8",
            )
        )

    ############################################################

    def load_page(
        self,
        filepath: Path,
    ) -> PageData:

        return PageData.model_validate_json(
            filepath.read_text(
                encoding="utf-8",
            )
        )

    ############################################################

    def load_pages(
        self,
        run_directory: Path,
    ) -> list[PageData]:

        pages_directory = (
            run_directory
            / "pages"
        )

        pages = []

        if not pages_directory.exists():
            return pages

        for file in sorted(
            pages_directory.glob("*.json")
        ):

            pages.append(
                self.load_page(file)
            )

        return pages

    ############################################################
    # RUN MANAGEMENT
    ############################################################

    def list_runs(
        self,
        source: str = "website",
    ) -> list[Path]:

        directory = (
            self.root
            / source
        )

        if not directory.exists():
            return []

        return sorted(
            [
                folder
                for folder in directory.iterdir()
                if folder.is_dir()
            ]
        )

    ############################################################

    def latest_run(
        self,
        source: str = "website",
    ) -> Path:

        runs = self.list_runs(source)

        if not runs:

            raise FileNotFoundError(
                "No crawl runs found."
            )

        return runs[-1]

    ############################################################

    def load_latest_crawl(
        self,
    ) -> CrawlResult:

        return self.load_crawl(
            self.latest_run()
        )

    ############################################################

    def load_latest_website(
        self,
    ) -> WebsiteData:

        return self.load_website(
            self.latest_run()
        )

    ############################################################

    def load_latest_pages(
        self,
    ) -> list[PageData]:

        return self.load_pages(
            self.latest_run()
        )

    ############################################################

    def latest_directory(
        self,
    ) -> Path:

        return self.latest_run()

    ############################################################

    def delete_run(
        self,
        run_directory: Path,
    ):

        import shutil

        if run_directory.exists():

            shutil.rmtree(run_directory)

            logger.warning(
                f"Deleted {run_directory}"
            )