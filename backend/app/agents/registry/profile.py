from dataclasses import dataclass


@dataclass
class AgentProfile:

    name: str

    memories: list

    documents: list

    workspace: list

    architecture: bool

    review: bool

    session: bool

    tools: list