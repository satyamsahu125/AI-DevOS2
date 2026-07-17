"""
Context Budget

Responsible for limiting the amount of
information passed to the LLM.

Phase 1
-------
Returns the context unchanged.

Future
------
- Token counting
- Context compression
- Priority ranking
- Automatic trimming
"""


class ContextBudget:

    def trim(
        self,
        context,
    ):

        return context