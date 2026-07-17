"""
Agent Context

The AgentContext is the only object consumed by
agents.

Agents never communicate with MemoryManager,
Workspace or Workflow directly.
"""

from dataclasses import dataclass, field


@dataclass
class AgentContext:

    project: str

    stage: str

    task: str

    memory: dict = field(default_factory=dict)

    workspace: dict = field(default_factory=dict)

    documents: dict = field(default_factory=dict)

    review: dict = field(default_factory=dict)

    runtime: dict = field(default_factory=dict)

    metadata: dict = field(default_factory=dict)