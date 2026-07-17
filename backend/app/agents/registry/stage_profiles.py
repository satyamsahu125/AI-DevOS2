"""
Stage Profiles
==============

Central registry of every workflow stage.

Each StageProfile defines:

• Agent implementation
• Prompt template
• Memory permissions
• Workspace permissions
• Documents
"""

from app.agents.implementations.product_owner import ProductOwner
from app.agents.implementations.architect import Architect
from app.agents.implementations.backend_designer import BackendDesigner
from app.agents.implementations.frontend_designer import FrontendDesigner
from app.agents.implementations.qa import QA
from app.agents.implementations.devops import DevOps

from app.agents.registry.stage_profiles import StageProfile

from app.agents.implementations.developer import Developer

STAGE_PROFILES = {

    "ProductOwner": StageProfile(

        name="ProductOwner",

        prompt="product_owner.md",

        agent_class=ProductOwner,

        memories=[
            "business",
            "workflow",
        ],

        workspace_write=[
            "requirements",
        ],

    ),

    "Architect": StageProfile(

        name="Architect",

        prompt="architect.md",

        agent_class=Architect,

        memories=[
            "business",
            "architecture",
            "decision",
        ],

        documents=[
            "requirements.md",
        ],

        workspace_write=[
            "architecture",
        ],

        architecture_stage=True,

    ),

    "BackendDesigner": StageProfile(

        name="BackendDesigner",

        prompt="backend.md",

        agent_class=BackendDesigner,

        memories=[
            "architecture",
            "decision",
        ],

        documents=[
            "architecture.md",
        ],

        workspace_read=[
            "backend",
        ],

        workspace_write=[
            "backend",
        ],

    ),

    "FrontendDesigner": StageProfile(

        name="FrontendDesigner",

        prompt="frontend.md",

        agent_class=FrontendDesigner,

        memories=[
            "architecture",
        ],

        documents=[
            "architecture.md",
        ],

        workspace_read=[
            "frontend",
        ],

        workspace_write=[
            "frontend",
        ],

    ),

    "QA": StageProfile(

        name="QA",

        prompt="qa.md",

        agent_class=QA,

        memories=[
            "business",
            "issue",
        ],

        documents=[
            "requirements.md",
        ],

        workspace_read=[
            "backend",
            "frontend",
        ],

        workspace_write=[
            "tests",
        ],

    ),

    "DevOps": StageProfile(

        name="DevOps",

        prompt="devops.md",

        agent_class=DevOps,

        memories=[
            "architecture",
            "workflow",
        ],

        documents=[
            "deployment.md",
        ],

        workspace_read=[
            "deployment",
        ],

        workspace_write=[
            "deployment",
        ],

    ),
    "Developer": StageProfile(
        
        name="Developer",
    
        prompt="developer.md",
    
        agent_class=Developer,
    
        memories=[
            "architecture",
            "decision",
            "artifact",
        ],
    
        documents=[
            "architecture.md",
            "backend.md",
            "frontend.md",
        ],
    
        workspace_read=[
            "backend",
            "frontend",
        ],
    
        workspace_write=[
            "backend",
            "frontend",
        ],
    
    ),

}