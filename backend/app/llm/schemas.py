from pydantic import BaseModel


class LLMRequest(BaseModel):

    prompt: str

    system_prompt: str = ""

    temperature: float = 0.2

    max_tokens: int = 8192

class LLMResponse(BaseModel):
    content: str