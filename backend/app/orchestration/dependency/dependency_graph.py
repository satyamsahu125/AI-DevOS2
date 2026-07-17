"""
Dependency Graph
================

Defines stage dependencies for the workflow.

Unlike a simple stage sequence, this graph answers:

    Can stage X execute?

rather than

    What comes after stage X?

This allows:

• Parallel stages
• Fan-in dependencies
• Future conditional stages
• Dynamic workflows

The DependencyGraph never executes stages.
"""

from collections import defaultdict


class DependencyGraph:

    def __init__(self):

        #
        # Each stage lists the stages that MUST
        # complete before it can execute.
        #

        self.dependencies = {

            "ProductOwner": [],

            "Architect": [
                "ProductOwner",
            ],

            "BackendDesigner": [
                "Architect",
            ],

            "FrontendDesigner": [
                "Architect",
            ],

            #
            # Both design stages must finish.
            #

            "Developer": [
                "BackendDesigner",
                "FrontendDesigner",
            ],

            "QA": [
                "Developer",
            ],

            "DevOps": [
                "QA",
            ],
        }

        #
        # Reverse lookup.
        #

        self.children = defaultdict(list)

        for stage, deps in self.dependencies.items():

            for dependency in deps:

                self.children[dependency].append(stage)

    # --------------------------------------------------

    def stages(self):

        return list(self.dependencies.keys())

    # --------------------------------------------------

    def exists(
        self,
        stage,
    ):

        return stage in self.dependencies

    # --------------------------------------------------

    def dependencies_of(
        self,
        stage,
    ):

        return self.dependencies.get(stage, [])

    # --------------------------------------------------

    def children_of(
        self,
        stage,
    ):

        return self.children.get(stage, [])

    # --------------------------------------------------

    def can_execute(
        self,
        stage,
        completed,
    ):
        """
        Returns True if all dependencies
        are completed.
        """

        required = self.dependencies_of(stage)

        return all(

            dependency in completed

            for dependency in required

        )

    # --------------------------------------------------

    def root_stages(self):
        """
        Stages with no dependencies.
        """

        return [

            stage

            for stage, deps in self.dependencies.items()

            if len(deps) == 0

        ]