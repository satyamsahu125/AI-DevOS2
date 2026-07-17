"""
Base Memory Interface

Every memory implementation inside AI DevOS must inherit from this class.

Responsibilities
----------------
- Define the standard contract for every memory.
- Hide the underlying storage implementation.
- Allow storage backends to change without affecting the framework.

Examples
--------
BusinessMemory
ArchitectureMemory
WorkflowMemory
ReviewMemory
WorkspaceMemory
ArtifactMemory
KnowledgeMemory

All implement the same interface.
"""

from abc import ABC, abstractmethod
from typing import Any


class BaseMemory(ABC):

    @abstractmethod
    def read(
        self,
        key: str,
    ) -> Any:
        """
        Read a value from memory.
        """
        pass

    @abstractmethod
    def write(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store or update a value.
        """
        pass

    @abstractmethod
    def delete(
        self,
        key: str,
    ) -> None:
        """
        Remove a value.
        """
        pass

    @abstractmethod
    def search(
        self,
        query: str,
    ):
        """
        Search memory.

        Phase 1:
            simple lookup

        Phase 3:
            semantic vector search
        """
        pass

    @abstractmethod
    def all(self):
        """
        Return every record.
        """
        pass