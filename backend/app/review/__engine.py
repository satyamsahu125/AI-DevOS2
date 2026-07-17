"""
Review Engine
=============

Coordinates the complete review subsystem.

Responsibilities

• Execute reviewer
• Parse review
• Decide retry
• Build reviewer feedback

The AI Kernel interacts ONLY with this class.
"""

from app.review.parser import ReviewParser
from app.review.decision import ReviewDecision
from app.review.feedback import ReviewFeedback


class ReviewEngine:

    def __init__(self):

        self.parser = ReviewParser()

        self.decision = ReviewDecision()

        self.feedback = ReviewFeedback()

    def review(

        self,

        reviewer_output: str,

        attempt: int,

        max_retry: int = 3,

    ):

        review = self.parser.parse(

            reviewer_output,

            attempt,

        )

        retry = self.decision.should_retry(

            review,

            max_retry,

        )

        feedback = self.feedback.format(

            review,

        )

        return review, retry, feedback