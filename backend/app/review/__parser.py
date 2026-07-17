"""
Review Parser
=============

Converts reviewer output into
ReviewResult.

Currently this parser is intentionally
simple.

Later it can support JSON validation,
Markdown parsing,
or structured schemas.
"""

from app.review.models import ReviewResult


class ReviewParser:

    def parse(

        self,

        reviewer_output: str,

        attempt: int,

    ) -> ReviewResult:

        text = reviewer_output.lower()

        approved = "approved" in text

        return ReviewResult(

            approved=approved,

            attempt=attempt,

            comments=reviewer_output,

        )