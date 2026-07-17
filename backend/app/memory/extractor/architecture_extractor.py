"""
Architecture Memory Extractor
=============================

Extracts architectural decisions.

Examples

• Components

• APIs

• Services

• Database Design

Writes into Architecture Memory.
"""

from app.memory.extractor.base_extractor import MemoryExtractor


class ArchitectureExtractor(MemoryExtractor):

    def extract(
        self,
        session,
        artifact,
        manager,
    ):

        pass