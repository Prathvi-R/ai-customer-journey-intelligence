from app.collectors.website import WebsiteCollector


async def main():

    collector = WebsiteCollector()

    await collector.collect(
        "https://shrreejisharan.com"
    )