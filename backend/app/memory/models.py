from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class MemoryRecord:

    key: str

    value: str

    source: str

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime = field(default_factory=datetime.utcnow)

    metadata: dict = field(default_factory=dict)