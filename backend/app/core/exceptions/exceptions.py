class AIDevOSError(Exception):
    """Base exception."""


class ConfigurationError(AIDevOSError):
    """Configuration error."""


class WorkflowError(AIDevOSError):
    """Workflow error."""


class MemoryError(AIDevOSError):
    """Memory error."""


class AgentError(AIDevOSError):
    """Agent execution error."""


class ReviewError(AIDevOSError):
    """Reviewer error."""