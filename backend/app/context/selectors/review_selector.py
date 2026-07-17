"""
Review Selector

Loads previous reviewer knowledge
relevant to the current stage.

Only reviewer summaries are returned.

The complete review history remains
inside Review Memory.
"""

from app.context.selectors.base_selector import BaseSelector


class ReviewSelector(BaseSelector):

    def load(
        self,
        stage: str,
        project: str,
    ):

        return {
            "feedback": [],
            "patterns": [],
        }