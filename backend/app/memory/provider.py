"""
Memory Provider

A generic in-memory implementation of BaseMemory.

Later versions can replace this with:

- PostgreSQL
- Redis
- Qdrant

without affecting the framework.
"""

from app.memory.base import BaseMemory
from app.memory.storage import MemoryStorage


class MemoryProvider(BaseMemory):

    def __init__(
        self,
        name: str,
    ):

        self.name = name

        self.storage = MemoryStorage()

    def read(
        self,
        key,
    ):

        return self.storage.get(key)

    def write(
        self,
        key,
        value,
    ):

        self.storage.put(
            key,
            value,
        )

    def delete(
        self,
        key,
    ):

        self.storage.delete(key)

    def search(
        self,
        query,
    ):

        results = {}

        for key, value in self.storage.all().items():

            if query.lower() in str(value).lower():

                results[key] = value

        return results

    def all(self):

        return self.storage.all()