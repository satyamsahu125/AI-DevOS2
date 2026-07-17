"""
Review Parser
=============

Converts raw reviewer output into a ReviewResult.

The parser is intentionally isolated so that
changing reviewer prompt formats never affects
WorkflowEngine.
"""

from app.review.review_result import ReviewResult


class ReviewParser:

    def parse(
        self,
        response: str,
        attempt: int,
    ) -> ReviewResult:

        approved = "APPROVED" in response.upper()

        return ReviewResult(

            approved=approved,

            comments=response,

            retry=not approved,

            attempt=attempt,

        )