"""
Developer Agent
===============

Converts approved designs into implementation plans.

Responsibilities

• Read approved architecture

• Read backend/frontend designs

• Generate implementation artifact

• Delegate code generation to Execution Engine

The Developer never edits files directly.

Only the Execution Engine modifies the workspace.
"""

from app.agents.base.base_agent import BaseAgent


class Developer(BaseAgent):

    NAME = "Developer"