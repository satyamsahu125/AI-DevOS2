"""
Kernel Runtime
--------------

Runtime holds everything required while a stage
is currently executing.

It exists only during execution.

Responsibilities
----------------
- Own ExecutionContext
- Own StageSession
- Track retries
- Track approval state

The Runtime is created by AIKernel and destroyed
after the stage finishes.
"""

from dataclasses import dataclass

from app.execution.execution_context import ExecutionContext
from app.session.stage_session import StageSession


@dataclass
class KernelRuntime:

    context: ExecutionContext

    session: StageSession

    retries: int = 0

    approved: bool = False

    finished: bool = False

    def retry(self):

        self.retries += 1

        self.session.retry()

    def approve(self):

        self.approved = True

        self.finished = True

        self.session.approve()

    def finish(self):

        self.finished = True