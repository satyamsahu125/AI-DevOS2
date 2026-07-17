from app.llm.providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):

    def chat(
        self,
        request,
    ):

        raise NotImplementedError(
            "Ollama provider not implemented."
        )