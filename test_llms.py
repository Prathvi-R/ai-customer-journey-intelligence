from dotenv import load_dotenv

load_dotenv()

import asyncio

from app.models.llm import LLMProvider
from app.services.llm import LLMService


async def main():

    providers = [

        (LLMProvider.OPENAI, "gpt-5-mini"),

        (LLMProvider.GEMINI, "gemini-2.5-flash"),

        (LLMProvider.CLAUDE, "claude-sonnet-4"),

        (LLMProvider.GROQ, "llama-3.3-70b-versatile"),

        (LLMProvider.OPENROUTER, "deepseek/deepseek-chat-v3"),

    ]

    for provider, model in providers:

        print(f"\nTesting {provider.value}...")

        try:

            llm = LLMService(
                provider=provider,
                model=model,
            )

            response = await llm.generate(
                system_prompt="You are a helpful assistant.",
                user_prompt="Reply with exactly: OK",
            )

            print(response)

        except Exception as e:

            print(e)


asyncio.run(main())