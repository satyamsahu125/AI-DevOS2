"""
Execution Engine
================

Only component allowed to modify
the project workspace.

Responsibilities

• Execute stage artifacts
• Create files
• Update files
• Delete files
• Notify Workspace Registry

Future

• Aider
• OpenHands
• Codex
• Cursor
"""

from app.workspace.registry import WorkspaceRegistry


class ExecutionEngine:

    def __init__(self):

        self.workspace = WorkspaceRegistry()

    # -----------------------------------------------------

    def execute(

        self,

        artifact,

        project,

    ):

        """
        Execute a StageArtifact.

        Current Version

        Placeholder.

        Future

        • Create files

        • Modify files

        • Run Aider

        """

        return self.backend.execute(
            artifact,
            project,
        )