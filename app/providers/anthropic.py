import os

import anthropic

from app.providers.base import BaseProvider


class AnthropicProvider(BaseProvider):

    def __init__(
        self,
        model: str,
    ):

        self.model = model

        self.client = anthropic.AsyncAnthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )

    async def generate(

        self,

        system_prompt: str,

        user_prompt: str,

        temperature: float = 0.2,

    ) -> str:

        response = await self.client.messages.create(

            model=self.model,

            system=system_prompt,

            temperature=temperature,

            max_tokens=4096,

            messages=[

                {
                    "role": "user",
                    "content": user_prompt,
                }

            ],

        )

        return response.content[0].text