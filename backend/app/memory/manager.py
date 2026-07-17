"""
Memory Manager
==============

Single entry point for every memory operation.

Owns every memory type.

Nothing writes directly into memory.
"""

from app.memory.pipeline.extraction_pipeline import ExtractionPipeline
from app.memory.provider import MemoryProvider
from app.memory.runtime.runtime_store import RuntimeStore


class MemoryManager:

    def __init__(self):

        self.pipeline = ExtractionPipeline()

        #
        # Runtime Memory
        #

        self.runtime_store = RuntimeStore()

        #
        # Long-term Memories
        #

        self.providers = {

            "business": MemoryProvider(),

            "architecture": MemoryProvider(),

            "workflow": MemoryProvider(),

            "review": MemoryProvider(),

            "decision": MemoryProvider(),

            "issue": MemoryProvider(),

            "artifact": MemoryProvider(),

        }

    # --------------------------------------------------

    def provider(

        self,

        name,

    ):

        provider = self.providers.get(name)

        if provider is None:

            raise ValueError(

                f"Unknown memory provider: {name}"

            )

        return provider

    # --------------------------------------------------

    def read(

        self,

        provider,

        key,

    ):

        return self.provider(provider).read(

            key,

        )

    # --------------------------------------------------

    def write(

        self,

        provider,

        key,

        value,

    ):

        self.provider(provider).write(

            key,

            value,

        )

    # --------------------------------------------------

    def delete(

        self,

        provider,

        key,

    ):

        self.provider(provider).delete(

            key,

        )

    # --------------------------------------------------

    def runtime(

        self,

        project,

        stage,

    ):

        """
        Return RuntimeMemory for one stage.
        """

        return self.runtime_store.get_or_create(

            project,

            stage,

        )

    # --------------------------------------------------

    def extract(

        self,

        session,

        artifact,

    ):

        self.pipeline.execute(

            session=session,

            artifact=artifact,

            manager=self,

        )