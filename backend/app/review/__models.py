"""
Review Models
=============

Contains strongly typed review objects.

The review subsystem returns ReviewResult
to the AI Kernel.

The kernel decides whether another execution
cycle is required.
"""

from dataclasses import dataclass, field


@dataclass
class ReviewResult:

    #
    # True when reviewer accepts output
    #

    approved: bool

    #
    # Retry number
    #

    attempt: int = 1

    #
    # Reviewer comments
    #

    comments: str = ""

    #
    # Structured improvements
    #

    improvements: list[str] = field(default_factory=list)

    #
    # Metadata
    #

    metadata: dict = field(default_factory=dict)