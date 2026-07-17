"""
Backend Designer Agent
======================

Designs backend components.

Responsibilities

• APIs

• Database

• Services

• Contracts

This agent only generates backend design.

It never writes source code.
"""

from app.agents.base.base_agent import BaseAgent


class BackendDesigner(BaseAgent):

    NAME = "BackendDesigner"