"""
Workspace
=========

Represents one indexed project workspace.
"""

from dataclasses import dataclass, field

from app.workspace.workspace_index import WorkspaceIndex


@dataclass
class Workspace:

    project_id: str

    root: str

    files: dict[str, WorkspaceIndex] = field(default_factory=dict)

    def register(
        self,
        index: WorkspaceIndex,
    ):

        self.files[index.path] = index

    def get(
        self,
        path: str,
    ):

        return self.files.get(path)

    def remove(
        self,
        path: str,
    ):

        self.files.pop(path, None)

    def list(self):

        return list(self.files.values())