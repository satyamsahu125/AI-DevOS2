"""
Memory Registry

The registry knows every memory module
available inside the platform.

It does NOT read or write memory.

It simply maps names
to memory implementations.
"""

from app.memory.base import BaseMemory


class MemoryRegistry:

    def __init__(self):

        self._memories = {}

    def register(
        self,
        name: str,
        memory: BaseMemory,
    ):

        self._memories[name] = memory

    def get(
        self,
        name: str,
    ) -> BaseMemory:

        memory = self._memories.get(name)

        if memory is None:

            raise ValueError(
                f"Unknown memory: {name}"
            )

        return memory

    def exists(
        self,
        name: str,
    ) -> bool:

        return name in self._memories

    def names(self):

        return list(
            self._memories.keys()
        )