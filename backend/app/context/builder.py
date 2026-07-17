"""
Context Builder

The Context Builder coordinates all selectors and
constructs the AgentContext.

It NEVER reads memory directly.
It NEVER scans the workspace.
It NEVER loads documents.

Its only responsibility is orchestration.
"""

from app.context.context import AgentContext
from app.context.budget import ContextBudget

from app.context.selectors.memory_selector import MemorySelector
from app.context.selectors.workspace_selector import WorkspaceSelector
from app.context.selectors.document_selector import DocumentSelector
from app.context.selectors.review_selector import ReviewSelector


class ContextBuilder:

    def __init__(self):

        self.memory = MemorySelector()

        self.workspace = WorkspaceSelector()

        self.documents = DocumentSelector()

        self.review = ReviewSelector()

        self.budget = ContextBudget()

    def build(
        self,
        project: str,
        stage: str,
        task: str,
    ) -> AgentContext:

        context = AgentContext(

            project=project,

            stage=stage,

            task=task,

        )

        context.memory = self.memory.load(
            stage,
            project,
        )

        context.workspace = self.workspace.load(
            stage,
            project,
        )

        context.documents = self.documents.load(
            stage,
            project,
        )

        context.review = self.review.load(
            stage,
            project,
        )

        return self.budget.trim(
            context,
        )