"""
Prompt Composer
===============

Builds the complete prompt for one stage.

Responsibilities

• Load system prompt
• Convert AgentContext into user prompt
• Populate StageSession

The composer never calls the LLM.
"""

from app.prompts.loader import PromptLoader


class PromptComposer:

    def __init__(self):

        self.loader = PromptLoader()

    def compose(

        self,

        profile,

        context,

        task,

    ):

        system_prompt = self.loader.load(

            profile.prompt,

        )

        user_prompt = f"""
# Task

{task}

# Context

{context}
"""

        return (

            system_prompt,

            user_prompt,

        )