"""
Prompt Renderer

Renders the final user prompt.

This is the only place where variables
are substituted.
"""


class PromptRenderer:

    def render(

        self,

        task,

        context,

    ):

        return f"""

# Task

{task}

---

# Context

{context}

""".strip()