"""
Dependency Manager

Facade around DependencyGraph.

Other modules should never use the graph
directly.
"""

from app.orchestration.dependency.dependency_graph import DependencyGraph


class DependencyManager:

    def __init__(self):

        self.graph = DependencyGraph()

    def execution_order(self):

        return self.graph.execution_order()

    def downstream(

        self,

        stage,

    ):

        return self.graph.downstream(stage)

    def node(

        self,

        stage,

    ):

        return self.graph.node(stage)