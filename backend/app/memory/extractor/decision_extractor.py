"""
Decision Memory Extractor
=========================

Stores important project decisions.

Examples

• Technology Choices

• Design Decisions

• Trade-offs

Writes into Decision Memory.
"""

from app.memory.extractor.base_extractor import MemoryExtractor


class DecisionExtractor(MemoryExtractor):

    def extract(
        self,
        session,
        artifact,
        manager,
    ):

        pass