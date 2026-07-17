from dataclasses import dataclass


@dataclass
class LLMSettings:

    provider: str = "gemini"

    model: str = ""

    temperature: float = 0.2


@dataclass
class DatabaseSettings:

    url: str = "sqlite:///aidevos.db"


@dataclass
class Settings:

    debug: bool = True

    llm: LLMSettings = LLMSettings()

    database: DatabaseSettings = DatabaseSettings()


settings = Settings()