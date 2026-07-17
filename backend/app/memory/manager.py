"""
Memory Manager
==============

Single entry point for every memory operation.

Responsibilities
----------------

• Read memories
• Write memories
• Delete memories
• Execute the extraction pipeline

Every memory type is owned by the MemoryManager.

Nothing writes directly into memory.
"""
from app.memory.runtime.runtime_store import RuntimeStore
from app.memory.pipeline.extraction_pipeline import ExtractionPipeline
from app.memory.provider import MemoryProvider


class MemoryManager:

    def __init__(self):

        self.pipeline = ExtractionPipeline()

        self.runtime = RuntimeStore()

        self.providers = {

            "business": MemoryProvider(),

            "architecture": MemoryProvider(),

            "workflow": MemoryProvider(),

            "review": MemoryProvider(),

            "decision": MemoryProvider(),

            "issue": MemoryProvider(),

            "runtime": MemoryProvider(),

            "artifact": MemoryProvider(),

        }

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

    def read(
        self,
        provider,
        key,
    ):

        return self.provider(provider).read(key)

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

    def delete(
        self,
        provider,
        key,
    ):

        self.provider(provider).delete(key)

    def extract(
        self,
        session,
        artifact,
    ):
        """
        Extract approved knowledge into long-term memories.
        """

        self.pipeline.execute(
            session=session,
            artifact=artifact,
            manager=self,
        )
    def runtime(
        self,
        project,
        stage,
    ):
        return self.runtime.get_or_create(
            project,
            stage,
        )