from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from app.models.crawl import CrawlResult
from app.models.page import PageData
from app.models.website import WebsiteData
from app.utils.logger import logger


class StorageService:
    """
    Handles persistence of crawl results.

    Responsibilities:
    - Create crawl run directories
    - Save CrawlResult
    - Save WebsiteData
    - Save PageData
    """

    def __init__(self, root_directory: str = "data"):
        self.root = Path(root_directory)

    def create_run(self, source: str = "website") -> Path:
        """
        Creates a versioned crawl directory.

        Example:

        data/
            website/
                2026-07-01_14-35-21/
        """

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        run_directory = self.root / source / timestamp

        (run_directory / "pages").mkdir(
            parents=True,
            exist_ok=True,
        )

        (run_directory / "screenshots").mkdir(
            parents=True,
            exist_ok=True,
        )

        logger.info(f"Created crawl directory: {run_directory}")

        return run_directory

    def save_crawl(
        self,
        crawl: CrawlResult,
        run_directory: Path,
    ) -> None:

        filepath = run_directory / "crawl.json"

        filepath.write_text(
            crawl.model_dump_json(indent=4),
            encoding="utf-8",
        )

        logger.success(f"Saved {filepath}")

    def save_website(
        self,
        website: WebsiteData,
        run_directory: Path,
    ) -> None:

        filepath = run_directory / "website.json"

        filepath.write_text(
            website.model_dump_json(indent=4),
            encoding="utf-8",
        )

        logger.success(f"Saved {filepath}")

    def save_page(
        self,
        page: PageData,
        run_directory: Path,
    ) -> None:

        slug = (
            page.url.replace("https://", "")
            .replace("http://", "")
            .replace("/", "_")
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

    def save_pages(
        self,
        website: WebsiteData,
        run_directory: Path,
    ) -> None:

        for page in website.pages:
            self.save_page(page, run_directory)

        logger.success(
            f"Saved {len(website.pages)} pages"
        )