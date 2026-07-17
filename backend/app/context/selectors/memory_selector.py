"""
Memory Selector
===============

Loads only the memories permitted for the
current workflow stage.

The permissions come directly from StageProfile.

MemorySelector never hardcodes stage names.
"""

from app.memory.manager import MemoryManager


class MemorySelector:

    def __init__(self):

        self.memory = MemoryManager()

    def load(
        self,
        profile,
        project,
    ):

        context = {}

        for memory_name in profile.memories:

            loader = getattr(
                self.memory,
                memory_name,
                None,
            )

            if callable(loader):

                context[memory_name] = loader(project)

        return context