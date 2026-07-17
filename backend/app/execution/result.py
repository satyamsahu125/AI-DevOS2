"""
Execution Result
================

Returned by the AgentExecutor after one stage.

This object is passed to:

WorkflowController
MemoryManager
WorkflowEngine

It contains everything needed to continue
execution.
"""

from dataclasses import dataclass, field


@dataclass
class ExecutionResult:

    stage: str

    output: str

    approved: bool

    review: str

    attempts: int

    metadata: dict = field(default_factory=dict)