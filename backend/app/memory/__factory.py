"""
Memory Factory

Responsible only for creating memory implementations.

It does NOT register them.

It does NOT manage them.

It simply constructs memory objects.
"""

from app.memory.provider import MemoryProvider


class MemoryFactory:

    def create(
        self,
        name: str,
    ):

        return MemoryProvider(
            name=name,
        )