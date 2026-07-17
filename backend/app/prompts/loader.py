"""
Prompt Loader
=============

Loads markdown prompt templates.

Future

• Variable substitution
• Prompt versioning
• Prompt registry
"""

from pathlib import Path


class PromptLoader:

    PROMPT_DIR = Path("prompts")

    def load(

        self,

        filename: str,

    ) -> str:

        path = self.PROMPT_DIR / filename

        if not path.exists():

            raise FileNotFoundError(

                f"Prompt not found: {filename}"

            )

        return path.read_text(

            encoding="utf-8"

        )