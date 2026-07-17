"""
Conversation Message
====================

Represents one message exchanged during a stage session.

This is the internal message format used throughout AI DevOS.

Providers are responsible for converting these messages into
their own API payload format.
"""

from dataclasses import dataclass


@dataclass
class Message:

    role: str

    content: str

    # -----------------------------------------------------

    def to_dict(self) -> dict:
        """
        Convert to provider-compatible format.
        """

        return {

            "role": self.role,

            "content": self.content,

        }