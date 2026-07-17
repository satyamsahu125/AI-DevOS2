"""
Product Owner Agent
===================

Transforms business ideas into structured requirements.

The ProductOwner agent relies entirely on the framework.

Responsibilities
----------------

• Understand business goals
• Produce requirement artifacts
• Define acceptance criteria

Implementation details such as prompt composition,
memory loading, review, and LLM execution are handled
by BaseAgent and the execution framework.
"""

from app.agents.base.base_agent import BaseAgent


class ProductOwner(BaseAgent):

    NAME = "ProductOwner"