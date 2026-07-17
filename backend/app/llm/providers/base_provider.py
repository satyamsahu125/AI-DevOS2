"""
Base Provider
=============

Abstract interface implemented by every LLM provider.

Examples

• Gemini

• Ollama

• OpenAI

• Claude

The framework never communicates with concrete
providers directly.
"""

from abc import ABC
from abc import abstractmethod

from app.llm.request import ChatRequest
from app.llm.response import ChatResponse


class BaseProvider(ABC):

    @abstractmethod
    def chat(
        self,
        request: ChatRequest,
    ) -> ChatResponse:
        """
        Execute a chat completion.
        """

        raise NotImplementedError