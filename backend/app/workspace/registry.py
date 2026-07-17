"""
Workspace Registry
==================

Indexes every project workspace.

Responsibilities

• Register workspaces
• Register files
• Lookup metadata
• Update metadata

Never reads file contents.
"""

from datetime import datetime

from app.workspace.workspace import Workspace
from app.workspace.workspace_index import WorkspaceIndex


class WorkspaceRegistry:

    def __init__(self):

        self.workspaces = {}

    # --------------------------------------------------

    def get_or_create(
        self,
        project_id: str,
        root: str,
    ) -> Workspace:

        workspace = self.workspaces.get(project_id)

        if workspace is None:

            workspace = Workspace(

                project_id=project_id,

                root=root,

            )

            self.workspaces[project_id] = workspace

        return workspace

    # --------------------------------------------------

    def register_file(
        self,
        project_id: str,
        root: str,
        path: str,
        module: str,
        file_type: str,
        checksum: str,
    ):

        workspace = self.get_or_create(

            project_id,

            root,

        )

        workspace.register(

            WorkspaceIndex(

                path=path,

                module=module,

                file_type=file_type,

                checksum=checksum,

                last_modified=datetime.utcnow(),

            )

        )

    # --------------------------------------------------

    def file(
        self,
        project_id: str,
        path: str,
    ):

        workspace = self.workspaces.get(project_id)

        if workspace is None:

            return None

        return workspace.get(path)

    # --------------------------------------------------

    def files(
        self,
        project_id: str,
    ):

        workspace = self.workspaces.get(project_id)

        if workspace is None:

            return []

        return workspace.list()

    # --------------------------------------------------

    def update_checksum(
        self,
        project_id: str,
        path: str,
        checksum: str,
    ):

        record = self.file(

            project_id,

            path,

        )

        if record is None:

            return

        record.checksum = checksum

        record.last_modified = datetime.utcnow()