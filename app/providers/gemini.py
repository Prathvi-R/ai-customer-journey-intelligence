import os

from google import genai

from app.providers.base import BaseProvider


class GeminiProvider(BaseProvider):

    def __init__(
        self,
        model: str,
    ):

        self.model = model

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    async def generate(

        self,

        system_prompt: str,

        user_prompt: str,

        temperature: float = 0.2,

    ) -> str:

        prompt = (
            system_prompt
            + "\n\n"
            + user_prompt
        )

        response = self.client.models.generate_content(

            model=self.model,

            contents=prompt,

        )

        return response.text