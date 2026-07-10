import asyncio

from app.pipeline.website_pipeline import WebsitePipeline


async def main():

    pipeline = WebsitePipeline(
        base_url="https://shrreejisharan.com",
        max_pages=5,
    )

    await pipeline.run()


if __name__ == "__main__":
    asyncio.run(main())