"""
Workspace Index
===============

Metadata describing one indexed file.

The registry stores metadata only.

File contents remain on disk.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class WorkspaceIndex:

    path: str

    module: str

    file_type: str

    checksum: str

    last_modified: datetime

    metadata: dict = field(default_factory=dict)