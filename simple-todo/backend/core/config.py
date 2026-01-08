from functools import lru_cache
from pathlib import Path

from pydantic import BaseModel, PostgresDsn
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


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    tasks: str = "/tasks"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


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
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig


@lru_cache
def get_settings() -> AppConfig:
    return AppConfig()
