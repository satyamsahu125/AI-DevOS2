"""
Stage Controller

Owns the complete lifecycle of one workflow stage.

Responsibilities

1. Create / Resume Stage Session
2. Execute Agent
3. Send output for review
4. Retry until approved
5. Close session
6. Return StageResult

This controller does NOT know how:

- LLM works
- Memory works
- Context is built
- Workflow moves forward

It only coordinates them.
"""

from app.execution.agent_executor import AgentExecutor
from app.review.review_engine import ReviewEngine
from app.session.session_manager import SessionManager

from app.stage.stage_result import StageResult
from app.stage.stage_status import StageStatus


class StageController:

    def __init__(self):

        self.sessions = SessionManager()

        self.executor = AgentExecutor()

        self.reviewer = ReviewEngine()

    def execute(
        self,
        stage_context,
    ) -> StageResult:

        """
        Execute one complete stage.

        Current implementation only defines the
        execution contract.

        Full retry loop will be added after
        Review Engine is completed.
        """

        raise NotImplementedError(
            "Stage execution pipeline is not implemented yet."
        )