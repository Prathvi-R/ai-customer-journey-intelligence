import os

from openai import AsyncOpenAI

from app.providers.base import BaseProvider


class OpenAIProvider(BaseProvider):

    def __init__(
        self,
        model: str,
    ):

        self.model = model

        self.client = AsyncOpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
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