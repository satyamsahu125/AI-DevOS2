"""
Memory Service

Public API of the Memory Framework.

No module communicates directly with
MemoryManager.
"""

from app.memory.manager import MemoryManager


class MemoryService:

    def __init__(self):

        self.manager = MemoryManager()

    def read(
        self,
        provider,
        key,
    ):

        return self.manager.read(

            provider,

            key,

        )

    def write(
        self,
        provider,
        key,
        value,
    ):

        self.manager.write(

            provider,

            key,

            value,

        )

    def delete(
        self,
        provider,
        key,
    ):

        self.manager.delete(

            provider,

            key,

        )