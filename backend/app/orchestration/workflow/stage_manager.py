"""
Stage Manager
=============

Owns workflow execution state.

Responsibilities
----------------

• Track lifecycle of every stage

• Determine executable stages

• Mark completed stages

• Handle retries

The StageManager never executes agents.
"""

from app.orchestration.dependency.dependency_graph import DependencyGraph
from app.orchestration.workflow.stage_state import StageState


class StageManager:

    def __init__(self):

        self.graph = DependencyGraph()

        self.state = {}

        #
        # Initialize every stage.
        #

        for stage in self.graph.stages():

            if len(self.graph.dependencies_of(stage)) == 0:

                self.state[stage] = StageState.READY

            else:

                self.state[stage] = StageState.WAITING

    # -------------------------------------------------

    def state_of(
        self,
        stage,
    ):

        return self.state[stage]

    # -------------------------------------------------

    def set_running(
        self,
        stage,
    ):

        self.state[stage] = StageState.RUNNING

    # -------------------------------------------------

    def complete(
        self,
        stage,
    ):

        self.state[stage] = StageState.COMPLETED

        #
        # Check children.
        #

        for child in self.graph.children_of(stage):

            if self.graph.can_execute(

                child,

                self.completed_set(),

            ):

                if self.state[child] == StageState.WAITING:

                    self.state[child] = StageState.READY

    # -------------------------------------------------

    def fail(
        self,
        stage,
    ):

        self.state[stage] = StageState.FAILED

    # -------------------------------------------------

    def retry(
        self,
        stage,
    ):

        self.state[stage] = StageState.READY

    # -------------------------------------------------

    def pause(
        self,
        stage,
    ):

        self.state[stage] = StageState.PAUSED

    # -------------------------------------------------

    def skip(
        self,
        stage,
    ):

        self.state[stage] = StageState.SKIPPED

    # -------------------------------------------------

    def available_stages(self):

        return [

            stage

            for stage, state in self.state.items()

            if state == StageState.READY

        ]

    # -------------------------------------------------

    def completed_set(self):

        return {

            stage

            for stage, state in self.state.items()

            if state == StageState.COMPLETED

        }

    # -------------------------------------------------

    def is_finished(self):

        return all(

            state in {

                StageState.COMPLETED,

                StageState.SKIPPED,

            }

            for state in self.state.values()

        )

    # -------------------------------------------------

    def reset(self):

        self.__init__()