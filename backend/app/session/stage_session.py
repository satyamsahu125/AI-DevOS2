"""
Stage Session

Represents the runtime conversation of ONE stage.

Lifecycle

Created
↓

Agent
↓

Reviewer
↓

Agent
↓

Reviewer

↓

Approved

↓

Destroyed

This object NEVER survives after approval.
"""

from dataclasses import dataclass, field
from datetime import datetime

from app.session.message import Message


@dataclass

class StageSession:

    project: str

    stage: str

    task: str

    conversation: list[Message] = field(default_factory=list)

    review_history: list[str] = field(default_factory=list)

    artifacts: dict = field(default_factory=dict)

    runtime: dict = field(default_factory=dict)

    metrics: dict = field(default_factory=dict)

    retries: int = 0

    approved: bool = False

    started_at: datetime = field(default_factory=datetime.utcnow)

    finished_at: datetime | None = None

    # -------------------------

    @property

    def is_started(self):

        return len(self.conversation) > 0

    # -------------------------

    def add_system(self, content):

        self.conversation.append(

            Message(

                role="system",

                content=content,

            )

        )

    def add_user(self, content):

        self.conversation.append(

            Message(

                role="user",

                content=content,

            )

        )

    def add_assistant(self, content):

        self.conversation.append(

            Message(

                role="assistant",

                content=content,

            )

        )

    def add_review(self, feedback):

        self.review_history.append(feedback)

        self.add_user(

            f"# Reviewer Feedback\n\n{feedback}"

        )

    def increment_retry(self):

        self.retries += 1

    def add_artifact(

        self,

        name,

        value,

    ):

        self.artifacts[name] = value

    def set_runtime(

        self,

        key,

        value,

    ):

        self.runtime[key] = value

    def complete(self):

        self.approved = True

        self.finished_at = datetime.utcnow()

    def messages(self):

        """
        Return strongly typed conversation.
    
        Providers convert Message objects into
        provider-specific payloads.
        """
    
        return self.conversation