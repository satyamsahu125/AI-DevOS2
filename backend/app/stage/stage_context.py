"""
Stage Context

Carries everything required to execute a single stage.

This object is created by the Workflow Engine and passed
through the Stage Controller to the Agent Executor.

It is intentionally immutable during execution except
for the attached StageSession.
"""

from dataclasses import dataclass

from app.agents.profile import StageProfile
from app.context.context import AgentContext


@dataclass
class StageContext:

    project: str

    stage: str

    task: str

    profile: StageProfile

    context: AgentContext