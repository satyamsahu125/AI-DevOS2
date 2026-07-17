"""
Workflow Engine
===============

The WorkflowEngine orchestrates an entire project workflow.

Responsibilities
----------------

• Start workflow
• Execute available stages
• Mark completed stages
• Continue until finished

It NEVER:

• Builds prompts
• Calls the LLM
• Reads memories
• Writes memories
• Executes code
• Reviews artifacts

Those responsibilities belong to dedicated modules.
"""

from app.agents.registry.agent_registry import AgentRegistry
from app.execution.agent_executor import AgentExecutor
from app.execution.execution_context import ExecutionContext
from app.orchestration.workflow.stage_manager import StageManager


class WorkflowEngine:

    def __init__(self):

        self.stage_manager = StageManager()

        self.registry = AgentRegistry()

        self.executor = AgentExecutor()

    # ---------------------------------------------------------

    def run(
        self,
        project,
    ):
        """
        Execute the complete project workflow.

        Returns
        -------
        dict

            {

                "results": [...],

                "success": bool

            }
        """

        results = []

        #
        # Continue until every stage completes.
        #

        while not self.stage_manager.is_finished():

            available = self.stage_manager.available_stages()

            #
            # Workflow finished.
            #

            if not available:

                break

            #
            # Execute every stage currently available.
            #

            for stage in available:

                profile = self.registry.profile(stage)

                context = ExecutionContext(

                    project=project,

                    stage=stage,

                    task=project.description,

                    profile=profile,

                    context=None,

                )

                #
                # Mark running.
                #

                self.stage_manager.set_running(stage)

                result = self.executor.execute(context)

                results.append(result)

                if result.approved:
                
                    self.stage_manager.complete(stage)

                else:
                
                    self.stage_manager.fail(stage)

        #
        # Finished
        #

        completed = len(
            self.stage_manager.completed_set()
        )

        total = len(

            self.stage_manager.graph.stages()

        )

        return {

            "results": results,

            "success": completed == total,

            "completed": completed,

            "total": total,

        }