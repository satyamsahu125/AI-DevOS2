"""
Session Service

Creates and manages Stage Sessions.

The service injects the active StageSession into
ExecutionContext.

The rest of AI DevOS never communicates with
SessionManager directly.
"""

from app.session.session_manager import SessionManager


class SessionService:

    def __init__(self):

        self.manager = SessionManager()

    def open(
        self,
        execution_context,
    ):

        execution_context.session = self.manager.get_or_create(

            project=execution_context.project,

            stage=execution_context.stage,

            task=execution_context.task,

        )

        return execution_context

    def approve(
        self,
        execution_context,
    ):

        if execution_context.session:

            execution_context.session.approve()

        execution_context.approved = True

        return execution_context

    def close(
        self,
        execution_context,
    ):

        self.manager.close(

            execution_context.project,

            execution_context.stage,

        )

        execution_context.session = None

        return execution_context