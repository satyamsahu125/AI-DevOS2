"""
QA Agent
========

Validates generated software.

Responsibilities

• Produce test strategy

• Generate test cases

• Detect issues

• Validate requirements

Execution of tests is delegated to future tooling.
"""

from app.agents.base.base_agent import BaseAgent


class QA(BaseAgent):

    NAME = "QA"