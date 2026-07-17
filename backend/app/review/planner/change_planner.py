"""
Change Planner
==============

Extracts actionable reviewer feedback.

Future versions may generate structured
patch instructions for Aider.

Current Version

Returns reviewer comments unchanged.
"""


class ChangePlanner:

    def build(
        self,
        review_result,
    ):

        return review_result.comments