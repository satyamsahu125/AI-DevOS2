"""
Business Memory Extractor
=========================

Extracts business knowledge from an approved stage.

Examples

• Requirements

• Business Rules

• Functional Constraints

Writes into Business Memory.
"""

from app.memory.extractor.base_extractor import MemoryExtractor


class BusinessExtractor(MemoryExtractor):

    def extract(
        self,
        session,
        artifact,
        manager,
    ):

        #
        # TODO:
        # Parse approved artifact.
        # Store only business knowledge.
        #

        pass