"""
Workspace Selector

Selects only the workspace information required
for the current stage.

The selector never scans the project directly.

In Phase 1 this returns an empty structure.

Later it will communicate with the Workspace Registry.
"""

from app.context.selectors.base_selector import BaseSelector


class WorkspaceSelector(BaseSelector):

    def load(
        self,
        stage: str,
        project: str,
    ):

        return {
            "files": [],
            "directories": [],
            "dependencies": [],
        }