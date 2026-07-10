from app.models.llm import TaskType
from app.services.llm import LLMService


class ModelRouter:

    @staticmethod
    def planner():

        return LLMService.recommended(
            TaskType.CHEAP
        )

    ###########################################################

    @staticmethod
    def persona():

        return LLMService.recommended(
            TaskType.EXTRACTION
        )

    ###########################################################

    @staticmethod
    def journey():

        return LLMService.recommended(
            TaskType.REASONING
        )

    ###########################################################

    @staticmethod
    def ux():

        return LLMService.recommended(
            TaskType.REASONING
        )

    ###########################################################

    @staticmethod
    def strategy():

        return LLMService.recommended(
            TaskType.REASONING
        )

    ###########################################################

    @staticmethod
    def copy():

        return LLMService.recommended(
            TaskType.CHEAP
        )

    ###########################################################

    @staticmethod
    def seo():

        return LLMService.recommended(
            TaskType.EXTRACTION
        )

    ###########################################################

    @staticmethod
    def trust():

        return LLMService.recommended(
            TaskType.REASONING
        )

    ###########################################################

    @staticmethod
    def report():

        return LLMService.recommended(
            TaskType.REASONING
        )