from abc import ABC, abstractmethod

from app.llm.schemas import LLMRequest, LLMResponse


class BaseLLM(ABC):
    """
    Base interface for every LLM provider.
    """

    @abstractmethod
    def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:
        pass
    
    @abstractmethod
    def chat(
        self,
        request,
    ):
        raise NotImplementedError