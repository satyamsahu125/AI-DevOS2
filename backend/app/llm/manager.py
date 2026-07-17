"""
LLM Manager
===========

Public entry point for every LLM request.

Responsibilities
----------------

• Accept ChatRequest
• Delegate execution to LLMRuntime
• Return ChatResponse

The manager contains NO provider logic.
"""

from app.llm.request import ChatRequest
from app.llm.response import ChatResponse
from app.llm.runtime import LLMRuntime


class LLMManager:

    def __init__(self):

        self.runtime = LLMRuntime()

    # ---------------------------------------------------------

    def chat(
        self,
        request: ChatRequest,
    ) -> ChatResponse:
        """
        Execute one chat request.
        """

        return self.runtime.chat(
            request,
        )