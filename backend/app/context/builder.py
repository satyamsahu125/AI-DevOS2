"""
Context Builder
===============

Coordinates all selectors and constructs the AgentContext.

Responsibilities

• Load permitted memories
• Load workspace metadata
• Load project documents
• Load previous reviews
• Load runtime memory
• Apply context budget

The Context Builder NEVER

• Reads memory directly
• Executes agents
• Calls the LLM
"""

from app.context.context import AgentContext
from app.context.budget import ContextBudget

from app.context.selectors.memory_selector import MemorySelector
from app.context.selectors.workspace_selector import WorkspaceSelector
from app.context.selectors.document_selector import DocumentSelector
from app.context.selectors.review_selector import ReviewSelector

from app.memory.manager import MemoryManager


class ContextBuilder:

    def __init__(

        self,

        memory_manager: MemoryManager,

    ):

        self.memory = memory_manager

        self.memory_selector = MemorySelector(self.memory)

        self.workspace_selector = WorkspaceSelector()

        self.document_selector = DocumentSelector()

        self.review_selector = ReviewSelector()

        self.budget = ContextBudget()

    # ---------------------------------------------------------

    def build(

        self,

        project,

        profile,

        stage,

        task,

    ) -> AgentContext:

        context = AgentContext(

            project=project,

            stage=stage,

            task=task,

        )

        #
        # Runtime Memory
        #

        context.runtime = self.memory.runtime(
            project.id,
            stage,
        )

        #
        # Long-term Memories
        #

        context.memory = self.memory_selector.load(

            profile=profile,

            project=project,

        )

        #
        # Workspace
        #

        context.workspace = self.workspace_selector.load(

            stage=stage,

            project=project,

        )

        #
        # Documents
        #

        context.documents = self.document_selector.load(

            stage=stage,

            project=project,

        )

        #
        # Previous Reviews
        #

        context.review = self.review_selector.load(

            stage=stage,

            project=project,

        )

        return self.budget.trim(

            context,

        )