"""
Agent Registry
==============

Factory responsible for creating stateless agents.

Responsibilities
----------------

• Return StageProfile

• Create Agent instances

• Validate stage names

This is the only place that knows which class
implements each workflow stage.
"""

from app.agents.registry.stage_profiles import STAGE_PROFILES


class AgentRegistry:

    def profile(
        self,
        stage: str,
    ):

        profile = STAGE_PROFILES.get(stage)

        if profile is None:

            raise ValueError(

                f"Unknown stage: {stage}"

            )

        return profile

    def create(
        self,
        stage: str,
    ):

        profile = self.profile(stage)

        return profile.agent_class(profile)