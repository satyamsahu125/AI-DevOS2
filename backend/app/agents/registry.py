from app.agents.capabilities import STAGE_PROFILES


class AgentRegistry:

    def profile(

        self,

        stage,

    ):

        profile = STAGE_PROFILES.get(stage)

        if profile is None:

            raise ValueError(

                f"Unknown stage: {stage}"

            )

        return profile