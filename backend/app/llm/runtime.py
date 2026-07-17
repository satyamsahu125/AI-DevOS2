"""
LLM Runtime
===========

Shared runtime used by every AI agent.

Responsibilities

• Select provider
• Execute ChatRequest
• Return ChatResponse
"""

from app.llm.provider_factory import ProviderFactory
from app.llm.request import ChatRequest
from app.llm.response import ChatResponse


class LLMRuntime:

    def __init__(self):

        self.factory = ProviderFactory()

    # ---------------------------------------------------------

    def chat(
        self,
        request: ChatRequest,
    ) -> ChatResponse:

        provider = self.factory.create()

        return provider.chat(
            request,
        )