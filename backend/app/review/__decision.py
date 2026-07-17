"""
Review Decision
===============

Contains retry policy.

The Review Engine asks this component
whether another execution should occur.
"""


class ReviewDecision:

    def should_retry(

        self,

        review,

        max_retry: int,

    ) -> bool:

        if review.approved:

            return False

        return review.attempt < max_retry