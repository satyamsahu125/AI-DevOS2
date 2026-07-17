"""
Runtime Memory
==============

Temporary memory used during one workflow stage.

Lifecycle

Stage starts
      │
      ▼
Runtime created
      │
      ▼
Agent
      │
      ▼
Reviewer
      │
      ▼
Retries
      │
      ▼
Approved
      │
      ▼
Destroyed

Runtime Memory is NEVER persisted.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class RuntimeMemory:

    project: str

    stage: str

    values: dict = field(default_factory=dict)

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime = field(default_factory=datetime.utcnow)

    # --------------------------------------------------

    def get(
        self,
        key,
        default=None,
    ):

        return self.values.get(

            key,

            default,

        )

    # --------------------------------------------------

    def set(
        self,
        key,
        value,
    ):

        self.values[key] = value

        self.updated_at = datetime.utcnow()

    # --------------------------------------------------

    def remove(
        self,
        key,
    ):

        self.values.pop(

            key,

            None,

        )

        self.updated_at = datetime.utcnow()

    # --------------------------------------------------

    def clear(self):

        self.values.clear()

        self.updated_at = datetime.utcnow()