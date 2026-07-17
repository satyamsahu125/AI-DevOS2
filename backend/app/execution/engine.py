"""
Execution Engine
================

Coordinates external code execution.

The engine delegates execution to the configured backend.
"""

from app.execution.aider.aider_backend import AiderBackend
from app.workspace.registry.workspace_registry import WorkspaceRegistry


class ExecutionEngine:

    def __init__(self):

        self.workspace = WorkspaceRegistry()

        self.backend = AiderBackend()

    # ---------------------------------------------------------

    def execute(

        self,

        artifact,

        project,

    ):

        return self.backend.execute(

            artifact,

            project,

        )