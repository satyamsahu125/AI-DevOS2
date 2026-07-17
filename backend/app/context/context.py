"""
Agent Context
=============

The AgentContext is the only object consumed by
agents.

Agents never communicate directly with

• MemoryManager
• Workspace
• Workflow
• Review Engine

Everything required for one execution is
prepared by the ContextBuilder.
"""

from dataclasses import dataclass, field

from app.memory.runtime.runtime_memory import RuntimeMemory


@dataclass(slots=True)
class AgentContext:

    #
    # Workflow
    #

    project: object

    stage: str

    task: str

    #
    # Long-term Memories
    #

    memory: dict = field(default_factory=dict)

    #
    # Workspace
    #

    workspace: dict = field(default_factory=dict)

    #
    # Documents
    #

    documents: dict = field(default_factory=dict)

    #
    # Previous Reviews
    #

    review: dict = field(default_factory=dict)

    #
    # Runtime Memory
    #

    runtime: RuntimeMemory | None = None

    #
    # Extra Metadata
    #

    metadata: dict = field(default_factory=dict)