from pathlib import Path

# Root
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Application
APP_NAME = "AI DevOS"

VERSION = "2.0"

# Storage
DATA_DIR = PROJECT_ROOT / "data"

MEMORY_DIR = DATA_DIR / "memory"

WORKSPACE_DIR = DATA_DIR / "workspace"

ARTIFACT_DIR = DATA_DIR / "artifacts"

LOG_DIR = DATA_DIR / "logs"

PROMPT_DIR = PROJECT_ROOT / "prompts"

# Default Models
DEFAULT_TEMPERATURE = 0.2