from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra='allow', env_file=Path(".env"))

    # SUPERSET
    SUPERSET_USER: str = 'admin'
    SUPERSET_PW: str = 'admin'
    SUPERSET_BASE_URL: str = 'http://127.0.0.1:8088'

    # BE_BASE_URL: str = 'http://127.0.0.1:8000/'


settings = Settings()
