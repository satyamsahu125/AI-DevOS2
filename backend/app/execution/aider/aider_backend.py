"""
Aider Backend
=============

Concrete execution backend using Aider.

This is currently the only implementation.

Future execution engines will implement the
same interface.
"""

from app.execution.backend import ExecutionBackend


class AiderBackend(ExecutionBackend):

    def execute(
        self,
        execution_plan,
    ):

        #
        # TODO
        #
        # Invoke aider
        # Update workspace
        # Return execution result
        #

        return None