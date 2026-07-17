from app.llm.providers.base_provider import BaseProvider


class GeminiProvider(BaseProvider):

    def chat(
        self,
        request,
    ):

        raise NotImplementedError(
            "Gemini provider not implemented."
        )