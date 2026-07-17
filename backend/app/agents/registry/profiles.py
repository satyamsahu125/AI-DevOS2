from app.core.agents.profile import AgentProfile

AGENT_PROFILES = {

    "ProductOwner": AgentProfile(
        name="ProductOwner",
        memories=["business", "workflow"],
        documents=["requirements.md"],
        workspace = {
            "read": [],
            "write": [],
        },
        architecture=False,
        review=True,
        session=True,
        tools=[],
    ),

    "Architect": AgentProfile(
        name="Architect",
        memories=["business", "architecture", "decision"],
        documents=["requirements.md"],
        workspace = {
            "read": [],
            "write": [],
        },
        architecture=True,
        review=True,
        session=True,
        tools=[],
    ),

    "FilePlanner": AgentProfile(
        name="FilePlanner",
        memories=["architecture"],
        documents=["architecture.md"],
        workspace = {
            "read": [],
            "write": [],
        },
        architecture=True,
        review=True,
        session=True,
        tools=[],
    ),

    "BackendDesigner": AgentProfile(
        name="BackendDesigner",
        memories=["architecture", "code", "decision"],
        documents=["architecture.md"],
        workspace = {
            "read": [
                "backend",
            ],
            "write": [
                "backend",
            ]
        },
        architecture=True,
        review=True,
        session=True,
        tools=[],
    ),

    "FrontendDesigner": AgentProfile(
        name="FrontendDesigner",
        memories=["architecture", "code"],
        documents=["architecture.md"],
        workspace = {
            "read": [
                "frontend",
            ],
            "write": [
                "frontend",
            ]
        },
        architecture=True,
        review=True,
        session=True,
        tools=[],
    ),

    "QA": AgentProfile(
        name="QA",
        memories=["business", "issue"],
        documents=["requirements.md"],
        workspace = {
            "read": [
                "backend",
                "frontend",
                "tests",
            ],
            "write": [
                "tests",
            ]
        },
        architecture=False,
        review=True,
        session=True,
        tools=[],
    ),

    "DevOps": AgentProfile(
        name="DevOps",
        memories=["architecture", "workflow"],
        documents=["deployment.md"],
        workspace={
            "read":["deployment"],
            "write":["deployment"]
        },
        architecture=True,
        review=True,
        session=True,
        tools=[],
    ),
}