"""
Prompt Formatter

Converts AgentContext into
human-readable sections.

No prompt logic lives here.
"""


class PromptFormatter:

    def format(self, context):

        sections = []

        if context.memory:

            sections.append(

                "# Memory\n\n"

                f"{context.memory}"

            )

        if context.documents:

            sections.append(

                "# Documents\n\n"

                f"{context.documents}"

            )

        if context.workspace:

            sections.append(

                "# Workspace\n\n"

                f"{context.workspace}"

            )

        if context.review:

            sections.append(

                "# Reviewer\n\n"

                f"{context.review}"

            )

        return "\n\n".join(sections)