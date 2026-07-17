"""
Architect Agent
===============

Creates the software architecture for the project.

Responsibilities

• Define architecture

• Design modules

• Define APIs

• Produce architecture artifacts

The framework handles all runtime behavior.
"""

from app.agents.base.base_agent import BaseAgent


class Architect(BaseAgent):

    NAME = "Architect"