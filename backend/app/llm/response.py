from dataclasses import dataclass


@dataclass
class ChatResponse:

    content: str

    prompt_tokens: int = 0

    completion_tokens: int = 0

    finish_reason: str = "stop"