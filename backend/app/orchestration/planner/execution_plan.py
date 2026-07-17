"""
Execution Plan

Represents the complete execution roadmap
for a project.

The Workflow Engine never iterates over raw
lists.

It always operates on an ExecutionPlan.
"""

from app.orchestration.planner.execution_step import ExecutionStep


class ExecutionPlan:

    def __init__(

        self,

        stages,

    ):

        self.steps = [

            ExecutionStep(stage)

            for stage in stages

        ]

        self.position = 0

    def finished(self):

        return self.position >= len(self.steps)

    def current(self):

        if self.finished():

            return None

        return self.steps[self.position]

    def next_step(self):

        if self.finished():

            return None

        step = self.steps[self.position]

        self.position += 1

        return step
    
    
    def previous(self):

        if self.position > 0:

            self.position -= 1

    def reset(self):

        self.position = 0