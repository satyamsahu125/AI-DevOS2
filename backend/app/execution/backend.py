"""
Execution Backend
=================

Abstract interface for code execution engines.

Supported implementations

• Aider
• OpenHands
• Cursor
• Future providers
"""

from abc import ABC
from abc import abstractmethod


class ExecutionBackend(ABC):

    @abstractmethod
    def execute(
        self,
        execution_plan,
    ):
        """
        Executes one execution plan.

        Returns
        -------
        ExecutionResult
        """