"""
Memory Permission Manager

The Memory Manager is the only component
allowed to modify memories.

Agents never write directly.

Before every read/write request,
Memory Manager asks PermissionManager
whether the operation is allowed.
"""


class MemoryPermissionManager:

    def __init__(self):

        self.permissions = {

            "ProductOwner": {

                "read": [
                    "business",
                    "workflow",
                ],

                "write": [
                    "business",
                    "workflow",
                ],
            },

            "Architect": {

                "read": [
                    "business",
                    "architecture",
                    "workflow",
                ],

                "write": [
                    "architecture",
                    "decision",
                ],
            },

            "BackendDesigner": {

                "read": [
                    "architecture",
                    "decision",
                    "workspace",
                ],

                "write": [
                    "workspace",
                    "artifact",
                ],
            },

            "FrontendDesigner": {

                "read": [
                    "architecture",
                    "workspace",
                ],

                "write": [
                    "workspace",
                    "artifact",
                ],
            },

            "QA": {

                "read": [
                    "business",
                    "workspace",
                    "artifact",
                ],

                "write": [
                    "qa",
                    "issues",
                    "review",
                ],
            },

            "DevOps": {

                "read": [
                    "architecture",
                    "workspace",
                    "artifact",
                ],

                "write": [
                    "workflow",
                ],
            },
        }

    def can_read(
        self,
        stage: str,
        memory: str,
    ) -> bool:

        config = self.permissions.get(stage)

        if config is None:
            return False

        return memory in config["read"]

    def can_write(
        self,
        stage: str,
        memory: str,
    ) -> bool:

        config = self.permissions.get(stage)

        if config is None:
            return False

        return memory in config["write"]