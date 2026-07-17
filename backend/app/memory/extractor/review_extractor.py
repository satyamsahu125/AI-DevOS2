"""
Review Memory Extractor
=======================

Extracts reviewer feedback.

Examples

• Common mistakes

• Review comments

• Improvement patterns

Writes into Review Memory.
"""

from app.memory.extractor.base_extractor import MemoryExtractor


class ReviewExtractor(MemoryExtractor):

    def extract(
        self,
        session,
        artifact,
        manager,
    ):

        pass