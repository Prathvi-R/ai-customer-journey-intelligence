import asyncio

from app.collectors.website import WebsiteCollector


async def main():

    collector = WebsiteCollector(
        base_url="https://shrreejisharan.com",
        max_pages=5,
    )

    result = await collector.collect()

    print("\n" + "=" * 60)
    print("CRAWL SUMMARY")
    print("=" * 60)

    print(f"Visited : {len(result.visited_urls)}")
    print(f"Failed  : {len(result.failed_urls)}")
    print(f"Pages   : {len(result.website_data.pages)}")

    print("=" * 60)

    for page in result.website_data.pages:

        print(f"\nTitle : {page.title}")
        print(f"URL   : {page.url}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    asyncio.run(main())