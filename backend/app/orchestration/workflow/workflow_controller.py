"""
Workflow Controller
===================

The Workflow Controller is responsible for deciding
how the workflow should progress after a stage finishes.

Responsibilities
----------------
• Continue to next stage
• Retry current stage
• Pause workflow
• Abort workflow
• Resume workflow (future)

The Workflow Controller DOES NOT execute agents.
It only makes workflow decisions.
"""

from enum import Enum


class WorkflowAction(str, Enum):

    CONTINUE = "CONTINUE"

    RETRY = "RETRY"

    PAUSE = "PAUSE"

    ABORT = "ABORT"

    COMPLETE = "COMPLETE"


class WorkflowController:

    def decide(
        self,
        execution_result,
    ):
        """
        Decide the next workflow action.

        Parameters
        ----------
        execution_result : ExecutionResult

        Returns
        -------
        WorkflowAction
        """

        # Reviewer approved
        if execution_result.approved:
            return WorkflowAction.CONTINUE

        # Retry current stage
        if execution_result.attempts < 3:
            return WorkflowAction.RETRY

        # Maximum retries exceeded
        return WorkflowAction.ABORT