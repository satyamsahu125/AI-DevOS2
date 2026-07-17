"""
Context Service

Builds AgentContext and injects it into the
ExecutionContext.
"""

from app.context.builder import ContextBuilder


class ContextService:

    def __init__(self):

        self.builder = ContextBuilder()

    def build(
        self,
        execution_context,
    ):

        execution_context.context = self.builder.build(

            project=execution_context.project,

            stage=execution_context.stage,

            task=execution_context.task,

        )

        return execution_context