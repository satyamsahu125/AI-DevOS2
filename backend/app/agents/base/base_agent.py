"""
Base Agent
==========

Base implementation of every AI DevOS agent.

Agents remain stateless.

Responsibilities

• Prepare LLM request
• Process LLM response
• Validate artifact
• Expose lifecycle hooks

Agents NEVER

• Call the LLM
• Build Context
• Load Memory
• Save Memory
• Update Workflow
• Modify Workspace
"""

from abc import ABC

from app.execution.stage_artifact import StageArtifact


class BaseAgent(ABC):

    NAME = ""

    def __init__(self, profile):

        self.profile = profile

    # -----------------------------------------------------

    def before_execute(
        self,
        context,
        session,
    ):
        """
        Optional initialization.
        """

        pass

    # -----------------------------------------------------

    def prepare(
        self,
        context,
        session,
    ):
        """
        Prepare messages for the LLM.

        Default:
            Entire session conversation.
        """

        return session.messages()

    # -----------------------------------------------------

    def process(
        self,
        response,
        context,
        session,
    ):
        """
        Convert ChatResponse into StageArtifact.
        """

        session.add_assistant(

            response.content,

        )

        return StageArtifact(

            stage=context.stage,

            content=response.content,

        )

    # -----------------------------------------------------

    def after_generate(
        self,
        artifact,
        context,
        session,
    ):
        """
        Optional post-processing.

        Example

        • Developer → Execution Engine

        • QA → Test Runner

        """

        return artifact

    # -----------------------------------------------------

    def validate(
        self,
        artifact,
    ):

        return