import os

from openai import AsyncOpenAI

from app.providers.base import BaseProvider


class OpenRouterProvider(BaseProvider):

    def __init__(
        self,
        model: str,
    ):

        self.model = model

        self.client = AsyncOpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
        )

    async def generate(

        self,

        system_prompt: str,

        user_prompt: str,

        temperature: float = 0.2,

    ) -> str:

        response = await self.client.chat.completions.create(

            model=self.model,

            temperature=temperature,

            messages=[

                {
                    "role": "system",
                    "content": system_prompt,
                },

                {
                    "role": "user",
                    "content": user_prompt,
                },

            ],

        )

        return response.choices[0].message.content