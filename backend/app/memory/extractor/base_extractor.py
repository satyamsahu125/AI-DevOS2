"""
Base Memory Extractor
=====================

Every extractor owns exactly one memory type.

Examples

BusinessExtractor

ArchitectureExtractor

ReviewExtractor

WorkflowExtractor

DecisionExtractor

The extractor converts an approved StageArtifact into
persistent knowledge.
"""

from abc import ABC
from abc import abstractmethod


class MemoryExtractor(ABC):

    @abstractmethod
    def extract(
        self,
        session,
        artifact,
        manager,
    ):
        """
        Read the approved StageSession and StageArtifact.

        Persist useful knowledge through MemoryManager.
        """

        raise NotImplementedError