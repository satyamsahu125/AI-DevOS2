from dataclasses import dataclass, field


@dataclass
class StageProfile:

    name: str

    prompt: str

    memories: list[str] = field(default_factory=list)

    documents: list[str] = field(default_factory=list)

    workspace_read: list[str] = field(default_factory=list)

    workspace_write: list[str] = field(default_factory=list)

    review_required: bool = True

    session: bool = True

    architecture: bool = False

    tools: list[str] = field(default_factory=list)