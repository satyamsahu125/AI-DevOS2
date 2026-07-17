"""
Runtime Memory Store
====================

Stores temporary RuntimeMemory objects.

Owned exclusively by MemoryManager.

Never accessed directly by agents.
"""

from app.memory.runtime.runtime_memory import RuntimeMemory


class RuntimeStore:

    def __init__(self):

        self._runtime = {}

    # --------------------------------------------------

    def _key(
        self,
        project,
        stage,
    ):

        return f"{project}:{stage}"

    # --------------------------------------------------

    def get(
        self,
        project,
        stage,
    ):

        return self._runtime.get(

            self._key(

                project,

                stage,

            )

        )

    # --------------------------------------------------

    def get_or_create(
        self,
        project,
        stage,
    ):

        runtime = self.get(

            project,

            stage,

        )

        if runtime is None:

            runtime = RuntimeMemory(

                project=project,

                stage=stage,

            )

            self._runtime[

                self._key(

                    project,

                    stage,

                )

            ] = runtime

        return runtime

    # --------------------------------------------------

    def remove(
        self,
        project,
        stage,
    ):

        self._runtime.pop(

            self._key(

                project,

                stage,

            ),

            None,

        )