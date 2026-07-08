from abc import ABC
from abc import abstractmethod


class BaseAgent(ABC):

    @abstractmethod
    async def run(
        self,
        question: str,
    ):
        ...