from dataclasses import dataclass
from typing import Any


@dataclass
class KernelEvent:

    name: str

    payload: Any = None