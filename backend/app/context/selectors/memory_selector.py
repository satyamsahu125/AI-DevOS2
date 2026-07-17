"""
Memory Selector

Responsible for selecting only the memory
required by the current stage.

It never reads memory directly.

Instead it communicates through MemoryService.
"""

from app.context.selectors.base_selector import BaseSelector
from app.memory.service import MemoryService


class MemorySelector(BaseSelector):

    def __init__(self):

        self.memory = MemoryService()

    def load(
        self,
        stage,
        project,
    ):

        result = {}

        memory_map = {

            "ProductOwner": [
                "business",
                "workflow",
            ],

            "Architect": [
                "business",
                "architecture",
            ],

            "BackendDesigner": [
                "architecture",
                "decision",
            ],

            "FrontendDesigner": [
                "architecture",
            ],

            "QA": [
                "business",
                "review",
                "issues",
            ],

            "DevOps": [
                "workflow",
                "architecture",
            ],

        }

        for memory in memory_map.get(stage, []):

            result[memory] = self.memory.read(

                stage=stage,

                memory=memory,

                key=project,

            )

        return result