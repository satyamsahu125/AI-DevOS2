"""
Review Feedback
===============

Formats reviewer comments before they
are injected back into the Stage Session.
"""


class ReviewFeedback:

    def format(

        self,

        review,

    ) -> str:

        return (

            "# Reviewer Feedback\n\n"

            f"{review.comments}"

        )