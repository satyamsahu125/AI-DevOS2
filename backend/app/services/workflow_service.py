"""
Workflow Service

Public entry point for workflow execution.

Future responsibilities

- Execute stages
- Resume workflows
- Retry stages
- Pause workflows
- Human approval
"""


class WorkflowService:

    def execute(
        self,
        project,
    ):

        raise NotImplementedError(
            "Workflow Engine not implemented yet."
        )