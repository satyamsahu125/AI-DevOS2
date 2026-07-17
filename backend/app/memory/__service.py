"""
Memory Service

The Memory Service is the public API for the entire
memory subsystem.

No module should access MemoryManager directly.

Responsibilities
----------------
- Expose simple read/write operations.
- Hide MemoryManager implementation.
- Become the integration point for caching,
  remote memory, metrics and future optimizations.
"""

from app.memory.bootstrap import MemoryBootstrap


class MemoryService:

    def __init__(self):

        self.manager = MemoryBootstrap().build()

    def read(
        self,
        stage: str,
        memory: str,
        key: str,
    ):

        return self.manager.read(

            stage=stage,

            memory=memory,

            key=key,

        )

    def write(
        self,
        stage: str,
        memory: str,
        key: str,
        value,
    ):

        self.manager.write(

            stage=stage,

            memory=memory,

            key=key,

            value=value,

        )

    def delete(
        self,
        stage: str,
        memory: str,
        key: str,
    ):

        self.manager.delete(

            stage=stage,

            memory=memory,

            key=key,

        )

    def audit(self):

        return self.manager.audit.all()