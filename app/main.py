import asyncio

from dotenv import load_dotenv

load_dotenv()

from app.pipeline.analyze import AnalysisPipeline


QUESTIONS = [

    "Who is the ideal customer?",

    "Improve homepage copy.",

    "How can SEO be improved?",

    "Increase trust on homepage.",

    "How should the website grow over the next year?",

    "Why are users leaving the website?",

]


async def main():

    pipeline = AnalysisPipeline()

    await pipeline.run(
        QUESTIONS
    )


if __name__ == "__main__":
    asyncio.run(main())