"""
Provider Factory
================

Creates the active LLM provider.

Only this class knows which provider is active.
"""

from app.core.config.settings import settings

from app.llm.providers.gemini import GeminiProvider
from app.llm.providers.ollama import OllamaProvider


class ProviderFactory:

    def create(self):

        provider = settings.llm.provider.lower()

        if provider == "gemini":

            return GeminiProvider()

        if provider == "ollama":

            return OllamaProvider()

        raise ValueError(

            f"Unsupported provider: {provider}"

        )