"""
Memory Audit Logger

Every successful memory write generates an audit entry.

Purpose
-------
- Full traceability
- Debugging
- Rollback support
- Future analytics

MemoryManager is the only component that writes
audit entries.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class AuditEntry:

    timestamp: datetime = field(default_factory=datetime.utcnow)

    stage: str = ""

    memory: str = ""

    key: str = ""

    action: str = ""

    previous_value: Any = None

    new_value: Any = None


class MemoryAudit:

    def __init__(self):

        self.entries: list[AuditEntry] = []

    def log(
        self,
        stage: str,
        memory: str,
        key: str,
        action: str,
        previous_value,
        new_value,
    ):

        self.entries.append(

            AuditEntry(

                stage=stage,

                memory=memory,

                key=key,

                action=action,

                previous_value=previous_value,

                new_value=new_value,

            )

        )

    def all(self):

        return self.entries

    def clear(self):

        self.entries.clear()