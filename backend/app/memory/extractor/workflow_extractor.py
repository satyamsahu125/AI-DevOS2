"""
Workflow Memory Extractor
=========================

Stores workflow progress.

Examples

• Completed Stages

• Current State

• Pending Work

Writes into Workflow Memory.
"""

from app.memory.extractor.base_extractor import MemoryExtractor


class WorkflowExtractor(MemoryExtractor):

    def extract(
        self,
        session,
        artifact,
        manager,
    ):

        pass