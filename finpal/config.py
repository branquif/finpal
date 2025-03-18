import os
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

CURRENT_DIR = Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent  # Raiz do projeto


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='allow')

    # Configuração base
    ENV: str = Field("development", validation_alias="FINPAL_ENV")
    SECRET_KEY: str = Field("chave_secreta_temporaria_para_desenvolvimento", validation_alias="FINPAL_SECRET_KEY")
    API_HOST: str = Field("localhost", validation_alias="FINPAL_API_HOST")
    API_PORT: int = Field(8000, validation_alias="FINPAL_API_PORT")
    DEFAULT_CURRENCY: str = Field("BRL", validation_alias="FINPAL_DEFAULT_CURRENCY")
    DATE_FORMAT: str = Field("DD/MM/YYYY", validation_alias="FINPAL_DATE_FORMAT")
    LANGUAGE: str = Field("pt-BR", validation_alias="FINPAL_LANGUAGE")

    # Caminho do banco de dados baseado no ambiente
    @property
    def DB_PATH(self) -> Path:
        env = self.ENV.lower()
        if env == "production":
            return BASE_DIR / "data" / "finpal.db"
        elif env == "testing":
            return BASE_DIR / "data" / "finpal_test.db"
        else:  # development é o padrão
            return BASE_DIR / "data" / "finpal_dev.db"


def get_settings():
    env = os.getenv("FINPAL_ENV", "development")

    # Seleciona o arquivo de ambiente correto
    if env == "production":
        env_file = BASE_DIR / "prod.env"
    elif env == "testing":
        env_file = BASE_DIR / "test.env"
    else:
        env_file = BASE_DIR / "dev.env"

    # Caso o arquivo específico não exista, usa o .env padrão
    if not env_file.exists():
        env_file = BASE_DIR / ".env"

    return Settings(_env_file=env_file if env_file.exists() else None)


settings = get_settings()
print(settings.DB_PATH)