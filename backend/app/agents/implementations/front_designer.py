"""
Frontend Designer Agent
=======================

Designs frontend architecture.

Responsibilities

• UI structure

• Components

• Navigation

• UX

This agent never edits frontend code.
"""

from app.agents.base.base_agent import BaseAgent


class FrontendDesigner(BaseAgent):

    NAME = "FrontendDesigner"