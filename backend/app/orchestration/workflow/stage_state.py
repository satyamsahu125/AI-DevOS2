"""
Stage State
===========

Defines the lifecycle of one workflow stage.

A stage always exists in exactly one state.

State Flow
----------

WAITING
    │
    ▼
READY
    │
    ▼
RUNNING
    │
    ├──────────────┐
    ▼              ▼
COMPLETED      FAILED
                   │
                   ▼
               READY (Retry)

The WorkflowEngine is responsible for moving
between states.

No other module may modify stage state.
"""

from enum import Enum


class StageState(str, Enum):

    #
    # Waiting for dependencies.
    #
    WAITING = "WAITING"

    #
    # Dependencies satisfied.
    #
    READY = "READY"

    #
    # Currently executing.
    #
    RUNNING = "RUNNING"

    #
    # Successfully completed.
    #
    COMPLETED = "COMPLETED"

    #
    # Reviewer rejected or execution failed.
    #
    FAILED = "FAILED"

    #
    # Human intervention required.
    #
    PAUSED = "PAUSED"

    #
    # Explicitly skipped.
    #
    SKIPPED = "SKIPPED"