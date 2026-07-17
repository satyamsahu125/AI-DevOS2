from app.prompts.registry import PROMPTS
from app.prompts.formatter import PromptFormatter
from app.constants.review_rules import REVIEW_RULES


class PromptBuilder:

    def build(
        self,
        agent,
        project,
        agent_context,
    ):

        template = PROMPTS[agent]

        # ----------------------------
        # Determine which agent is being reviewed
        # ----------------------------

        review_agent = agent

        if agent == "Reviewer":

            review_agent = agent_context.state.get(
                "last_agent",
                agent_context.state.get(
                    "current_stage",
                    "ProductOwner",
                ),
            )

        # ----------------------------
        # Load correct review rules
        # ----------------------------

        review_rules = PromptFormatter.review_rules(
            REVIEW_RULES.get(
                review_agent,
                "",
            )
        )

        current_agent = PromptFormatter.current_agent(
            review_agent,
        )

        # ----------------------------
        # Build Prompt
        # ----------------------------

        return template.format(

            project=PromptFormatter.project(project),

            architecture=PromptFormatter.architecture(
                agent_context.architecture,
            ),

            workspace=PromptFormatter.workspace(
                agent_context.workspace,
            ),

            documents=PromptFormatter.documents(
                agent_context.documents,
            ),

            memory=PromptFormatter.memory(
                agent_context.memory,
            ),

            state=PromptFormatter.state(
                agent_context.state,
            ),

            review_rules=review_rules,

            current_agent=current_agent,

            review=PromptFormatter.review(
                agent_context.review,
            ),
        )