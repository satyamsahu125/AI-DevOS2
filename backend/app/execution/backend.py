"""
Execution Backend
=================

Abstract interface implemented by every
code execution backend.

Examples

• Aider
• OpenHands
• Codex
• Cursor
"""

from abc import ABC
from abc import abstractmethod

from app.execution.stage_artifact import StageArtifact


class ExecutionBackend(ABC):

    @abstractmethod
    def execute(
        self,
        artifact: StageArtifact,
        project,
    ) -> StageArtifact:
        """
        Execute a StageArtifact.

        Returns the updated artifact.
        """
        raise NotImplementedError