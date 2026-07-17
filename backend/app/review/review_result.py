"""
Review Result
=============

Represents the reviewer decision for one stage.
"""

from dataclasses import dataclass, field


@dataclass
class ReviewResult:

    approved: bool

    comments: str

    retry: bool

    attempt: int

    metadata: dict = field(default_factory=dict)