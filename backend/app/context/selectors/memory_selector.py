"""
Memory Selector
===============

Loads only memories allowed by the StageProfile.

Memory permissions are defined ONLY in StageProfile.
"""

from app.memory.manager import MemoryManager


class MemorySelector:

    def __init__(

        self,

        manager: MemoryManager,

    ):

        self.manager = manager

    # ---------------------------------------------------------

    def load(

        self,

        profile,

        project,

    ):

        context = {}

        for memory_name in profile.memories:

            loader = getattr(

                self.manager,

                memory_name,

                None,

            )

            if callable(loader):

                context[memory_name] = loader(

                    project,

                )

        return context