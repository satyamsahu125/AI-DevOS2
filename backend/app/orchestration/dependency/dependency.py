"""
Dependency

Represents one workflow node.

The dependency graph is the single source of
truth for workflow relationships.
"""

from dataclasses import dataclass, field


@dataclass
class Dependency:

    stage: str

    requires: list[str] = field(default_factory=list)

    next: list[str] = field(default_factory=list)

    optional: list[str] = field(default_factory=list)