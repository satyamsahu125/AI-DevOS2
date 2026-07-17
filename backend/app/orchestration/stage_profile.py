"""
Stage Profile
=============

Defines the complete configuration for one workflow stage.

A StageProfile is configuration only.

It NEVER contains business logic.

Responsibilities
----------------

• Stage identity
• Prompt template
• Agent implementation
• LLM configuration
• Memory permissions
• Workspace permissions
• Document permissions
• Tool permissions

The AgentRegistry uses StageProfiles to create
fully configured Agent instances.
"""

from dataclasses import dataclass, field
from typing import Type

from app.agents.base.base_agent import BaseAgent


@dataclass(slots=True)
class StageProfile:
    """
    Configuration for one workflow stage.
    """

    # ======================================================
    # Stage Identity
    # ======================================================

    name: str

    # ======================================================
    # Prompt
    # ======================================================

    prompt: str

    # ======================================================
    # Agent
    # ======================================================

    agent_class: Type[BaseAgent]

    # ======================================================
    # LLM Configuration
    # ======================================================

    model: str

    temperature: float = 0.2

    max_tokens: int | None = None

    # ======================================================
    # Memory Permissions
    # ======================================================

    memories: list[str] = field(default_factory=list)

    # ======================================================
    # Documents
    # ======================================================

    documents: list[str] = field(default_factory=list)

    # ======================================================
    # Workspace Permissions
    # ======================================================

    workspace_read: list[str] = field(default_factory=list)

    workspace_write: list[str] = field(default_factory=list)

    # ======================================================
    # Optional Tools
    # ======================================================

    tools: list[str] = field(default_factory=list)

    # ======================================================
    # Behaviour
    # ======================================================

    review_required: bool = True

    session_enabled: bool = True

    architecture_stage: bool = False