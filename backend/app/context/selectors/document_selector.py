"""
Document Selector

Provides project documents needed by the stage.

Examples

- requirements.md
- architecture.md
- api_design.md

In Phase 1 this is only a placeholder.

Later it will communicate with the
Artifact Manager / Document Service.
"""

from app.context.selectors.base_selector import BaseSelector


class DocumentSelector(BaseSelector):

    def load(
        self,
        stage: str,
        project: str,
    ):

        return {
            "documents": []
        }