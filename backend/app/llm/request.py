from dataclasses import dataclass

from app.session.message import Message


@dataclass
class ChatRequest:
    """
    Standard chat request.

    Used by every provider.

    Providers convert this object into their
    own API format.
    """

    model: str

    messages: list[Message]

    temperature: float = 0.2

    max_tokens: int | None = None