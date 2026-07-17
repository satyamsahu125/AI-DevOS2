"""
DevOps Agent
============

Designs deployment and infrastructure.

Responsibilities

• Deployment

• Containers

• CI/CD

• Infrastructure

Infrastructure execution is delegated to the
Execution Engine.
"""

from app.agents.base.base_agent import BaseAgent


class DevOps(BaseAgent):

    NAME = "DevOps"