import ollama

from app.providers.base import BaseProvider


class OllamaProvider(BaseProvider):

    def __init__(
        self,
        model: str,
    ):

        self.model = model

    async def generate(

        self,

        system_prompt: str,

        user_prompt: str,

        temperature: float = 0.2,

    ) -> str:

        response = ollama.chat(

            model=self.model,

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

            options={

                "temperature": temperature,

            },

        )

        return response["message"]["content"]