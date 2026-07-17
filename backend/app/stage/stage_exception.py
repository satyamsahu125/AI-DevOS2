"""
Stage Exceptions

Contains all exceptions related to stage execution.
"""


class StageException(Exception):
    """Base exception for stage errors."""


class StageExecutionError(StageException):
    """Raised when agent execution fails."""


class StageReviewError(StageException):
    """Raised when reviewer execution fails."""


class StageSessionError(StageException):
    """Raised when a stage session becomes invalid."""