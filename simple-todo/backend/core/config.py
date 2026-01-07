from functools import lru_cache
from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_PATH = Path(__file__).parents[1].resolve()


class LoggingConfig(BaseModel):
    level: str = "INFO"
    rotation: str = "10 MB"
    retention: int = 3
    file_name: str = "simpletodo.log.jsonl"

    @property
    def log_path(self) -> Path:
        path = PROJECT_PATH / "logs"
        path.mkdir(exist_ok=True, parents=True)
        return path / self.file_name


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(
            PROJECT_PATH / ".env.template",
            PROJECT_PATH / ".env",
        ),
        env_prefix="APP__",
        env_nested_delimiter="__",
        case_sensitive=False,
        validate_assignment=True,
        extra="ignore",
    )

    logging: LoggingConfig = LoggingConfig()


@lru_cache
def get_settings() -> AppConfig:
    return AppConfig()
