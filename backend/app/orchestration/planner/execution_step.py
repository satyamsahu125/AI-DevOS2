"""
Execution Step

Represents one executable stage inside an
Execution Plan.

Future extensions

- parallel execution
- retry policy
- timeout
- human approval
- conditional execution
"""

from dataclasses import dataclass, field


@dataclass
class ExecutionStep:

    stage: str

    completed: bool = False

    skipped: bool = False

    retry_count: int = 0

    metadata: dict = field(default_factory=dict)

    def finish(self):

        self.completed = True

    def retry(self):

        self.retry_count += 1

    def skip(self):

        self.skipped = True