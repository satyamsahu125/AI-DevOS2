"""
Execution Context
=================

Shared execution state.

This object travels through the entire runtime.

AIKernel

↓

WorkflowEngine

↓

AgentExecutor

↓

BaseAgent
"""

from dataclasses import dataclass


@dataclass
class ExecutionContext:

    project: object

    workflow: object

    stage: str

    task: str

    profile: object

    context: object