"""
Session Manager
===============

Owns the lifecycle of Stage Sessions.

Responsibilities
----------------

• Create Stage Sessions
• Resume Stage Sessions
• Destroy Stage Sessions

The SessionManager NEVER stores long-term knowledge.

StageSessions exist only until the reviewer approves the stage.
"""

from app.session.stage_session import StageSession


class SessionManager:

    def __init__(self):

        self.sessions = {}

    def _key(
        self,
        project,
        stage,
    ):

        return f"{project}:{stage}"

    def get(
        self,
        project,
        stage,
    ):

        return self.sessions.get(
            self._key(project, stage)
        )

    def create(
        self,
        project,
        stage,
        task="",
    ):

        session = StageSession(
            project=project,
            stage=stage,
            task=task,
        )

        self.sessions[
            self._key(project, stage)
        ] = session

        return session

    def get_or_create(
        self,
        project,
        stage,
        task="",
    ):

        session = self.get(
            project,
            stage,
        )

        if session is None:

            session = self.create(
                project=project,
                stage=stage,
                task=task,
            )

        return session

    def close(
        self,
        project,
        stage,
    ):

        self.sessions.pop(
            self._key(project, stage),
            None,
        )