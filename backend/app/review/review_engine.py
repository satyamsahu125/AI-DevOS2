"""
Review Engine
=============

Coordinates the review process.

Responsibilities

• Ask reviewer LLM
• Parse review
• Produce ReviewResult

The Review Engine never retries stages.

It only returns the reviewer decision.
"""

from app.review.parser.review_parser import ReviewParser
from app.review.planner.change_planner import ChangePlanner


class ReviewEngine:

    def __init__(self):

        self.parser = ReviewParser()

        self.planner = ChangePlanner()

    def review(
        self,
        reviewer_response: str,
        attempt: int,
    ):

        result = self.parser.parse(

            reviewer_response,

            attempt,

        )

        result.metadata["changes"] = self.planner.build(

            result,

        )

        return result