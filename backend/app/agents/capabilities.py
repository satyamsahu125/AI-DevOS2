from app.agents.profile import StageProfile


STAGE_PROFILES = {

    "ProductOwner": StageProfile(

        name="ProductOwner",

        prompt="product_owner.md",

        memories=[

            "business",

            "workflow",

        ],

        documents=[],

        workspace_read=[],

        workspace_write=[

            "requirements",

        ],

        review_required=True,

    ),

    "Architect": StageProfile(

        name="Architect",

        prompt="architect.md",

        memories=[

            "business",

            "architecture",

        ],

        documents=[

            "requirements.md",

        ],

        workspace_read=[],

        workspace_write=[

            "architecture",

        ],

        architecture=True,

    ),

    "FilePlanner": StageProfile(

        name="FilePlanner",

        prompt="file_planner.md",

        memories=[

            "architecture",

        ],

        documents=[

            "architecture.md",

        ],

        workspace_write=[

            "workspace",

        ],

    ),

    "BackendDesigner": StageProfile(

        name="BackendDesigner",

        prompt="backend_designer.md",

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

        prompt="frontend_designer.md",

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

}