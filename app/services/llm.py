import traceback

from app.models.llm import (
    LLMModel,
    LLMProvider,
    TaskType,
)

from app.providers.anthropic import AnthropicProvider
from app.providers.gemini import GeminiProvider
from app.providers.groq import GroqProvider
from app.providers.ollama import OllamaProvider
from app.providers.openai import OpenAIProvider
from app.providers.openrouter import OpenRouterProvider


class LLMService:

    MODELS = [

        ########################################################
        # OpenAI
        ########################################################

        LLMModel(
            provider=LLMProvider.OPENAI,
            name="gpt-5",
            context_window=400000,
            reasoning_rank=5,
            speed_rank=4,
            supports_vision=True,
        ),

        LLMModel(
            provider=LLMProvider.OPENAI,
            name="gpt-5-mini",
            context_window=400000,
            reasoning_rank=4,
            speed_rank=5,
            cost_rank=5,
            supports_vision=True,
        ),

        ########################################################
        # Gemini
        ########################################################

        LLMModel(
            provider=LLMProvider.GEMINI,
            name="gemini-2.5-pro",
            context_window=1000000,
            reasoning_rank=5,
            supports_vision=True,
        ),

        LLMModel(
            provider=LLMProvider.GEMINI,
            name="gemini-2.5-flash",
            context_window=1000000,
            reasoning_rank=4,
            speed_rank=5,
            cost_rank=5,
            supports_vision=True,
        ),

        ########################################################
        # Claude
        ########################################################

        LLMModel(
            provider=LLMProvider.CLAUDE,
            name="claude-sonnet-4",
            context_window=200000,
            reasoning_rank=5,
        ),

        ########################################################
        # Groq
        ########################################################

        LLMModel(
            provider=LLMProvider.GROQ,
            name="llama-3.3-70b-versatile",
            context_window=131072,
            reasoning_rank=4,
            speed_rank=5,
        ),

        ########################################################
        # OpenRouter
        ########################################################

        LLMModel(
            provider=LLMProvider.OPENROUTER,
            name="deepseek/deepseek-chat-v3",
            context_window=128000,
            reasoning_rank=5,
            cost_rank=5,
        ),

        LLMModel(
            provider=LLMProvider.OPENROUTER,
            name="qwen/qwen3-235b-a22b",
            context_window=128000,
            reasoning_rank=5,
        ),

        ########################################################
        # Ollama
        ########################################################

        LLMModel(
            provider=LLMProvider.OLLAMA,
            name="llama3.2",
            context_window=128000,
        ),
    ]

    ##################################################################

    def __init__(
        self,
        provider: LLMProvider,
        model: str,
    ):

        self.provider = provider
        self.model = model

        self.client = self._create_provider()

    ##################################################################

    def _create_provider(self):

        if self.provider == LLMProvider.OPENAI:
            return OpenAIProvider(self.model)

        if self.provider == LLMProvider.GEMINI:
            return GeminiProvider(self.model)

        if self.provider == LLMProvider.CLAUDE:
            return AnthropicProvider(self.model)

        if self.provider == LLMProvider.GROQ:
            return GroqProvider(self.model)

        if self.provider == LLMProvider.OPENROUTER:
            return OpenRouterProvider(self.model)

        if self.provider == LLMProvider.OLLAMA:
            return OllamaProvider(self.model)

        raise ValueError(
            f"Unknown provider {self.provider}"
        )

    ##################################################################

    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
    ):

        fallback_chain = [

            (self.provider, self.model),

            (LLMProvider.GEMINI, "gemini-2.5-flash"),

            (LLMProvider.OPENROUTER, "deepseek/deepseek-chat-v3"),

            (LLMProvider.GROQ, "llama-3.3-70b-versatile"),

            (LLMProvider.OPENAI, "gpt-5-mini"),

            (LLMProvider.OLLAMA, "llama3.2"),

        ]

        tried = set()

        last_error = None

        for provider, model in fallback_chain:

            if (provider, model) in tried:
                continue

            tried.add((provider, model))

            try:

                print(
                    f"Trying {provider.value} ({model})..."
                )

                client = LLMService(
                    provider=provider,
                    model=model,
                ).client

                answer = await client.generate(
                    system_prompt,
                    user_prompt,
                    temperature,
                )

                print(
                    f"Using {provider.value}"
                )

                return answer

            except Exception as e:

                last_error = e

                print(
                    f"{provider.value} failed:"
                )

                print(e)

                traceback.print_exc()

                continue

        raise RuntimeError(
            f"All providers failed.\n\nLast error:\n{last_error}"
        )

    ##################################################################

    @classmethod
    def recommended(
        cls,
        task: TaskType,
    ):

        if task == TaskType.REASONING:

            return cls(
                provider=LLMProvider.GEMINI,
                model="gemini-2.5-flash",
            )

        if task == TaskType.CODING:

            return cls(
                provider=LLMProvider.OPENROUTER,
                model="deepseek/deepseek-chat-v3",
            )

        if task == TaskType.EXTRACTION:

            return cls(
                provider=LLMProvider.GEMINI,
                model="gemini-2.5-flash",
            )

        if task == TaskType.VISION:

            return cls(
                provider=LLMProvider.GEMINI,
                model="gemini-2.5-flash",
            )

        if task == TaskType.CHEAP:

            return cls(
                provider=LLMProvider.OPENROUTER,
                model="deepseek/deepseek-chat-v3",
            )

        if task == TaskType.LOCAL:

            return cls(
                provider=LLMProvider.OLLAMA,
                model="llama3.2",
            )

        return cls(
            provider=LLMProvider.GEMINI,
            model="gemini-2.5-flash",
        )

    ##################################################################

    @classmethod
    def available_models(cls):
        return cls.MODELS