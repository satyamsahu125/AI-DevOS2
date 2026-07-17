from app.prompts.product_owner import PRODUCT_OWNER_PROMPT
from app.prompts.architect import ARCHITECT_PROMPT
from app.prompts.backend import BACKEND_PROMPT
from app.prompts.frontend import FRONTEND_PROMPT
from app.prompts.qa import QA_PROMPT
from app.prompts.devops import DEVOPS_PROMPT
from app.prompts.reviewer import REVIEWER_PROMPT
from app.prompts.file_planner import FILE_PLANNER_PROMPT

PROMPTS = {

    "ProductOwner": PRODUCT_OWNER_PROMPT,

    "Architect": ARCHITECT_PROMPT,

    "FilePlanner": FILE_PLANNER_PROMPT,

    "BackendDesigner": BACKEND_PROMPT,

    "FrontendDesigner": FRONTEND_PROMPT,

    "QA": QA_PROMPT,

    "DevOps": DEVOPS_PROMPT,

    "Reviewer": REVIEWER_PROMPT,

}