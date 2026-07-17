"""
Execution Planner

Builds an ExecutionPlan from the
DependencyGraph.

No stage ordering is hardcoded.
"""

from app.orchestration.dependency.dependency_manager import DependencyManager
from app.orchestration.planner.execution_plan import ExecutionPlan


class ExecutionPlanner:

    def __init__(self):

        self.dependencies = DependencyManager()

    def build(

        self,

        execution_context,

    ):

        stages = self.dependencies.execution_order()

        return ExecutionPlan(

            stages,

        )