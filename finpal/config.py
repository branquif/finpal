import os
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# finpal/config.py
CURRENT_DIR = Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent  # Raiz do projeto (acima do diretório finpal)

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    ENV: str = Field("development", validation_alias="FINPAL_ENV")
    DB_PATH: Path = Field(BASE_DIR / "data" / "FINPAL.db", validation_alias="FINPAL_DB_PATH")
    SECRET_KEY: str = Field("chave_secreta_temporaria_para_desenvolvimento", validation_alias="FINPAL_SECRET_KEY")
    API_HOST: str = Field("localhost", validation_alias="FINPAL_API_HOST")
    API_PORT: int = Field(8000, validation_alias="FINPAL_API_PORT")
    DEFAULT_CURRENCY: str = Field("BRL", validation_alias="FINPAL_DEFAULT_CURRENCY")
    DATE_FORMAT: str = Field("DD/MM/YYYY", validation_alias="FINPAL_DATE_FORMAT")
    LANGUAGE: str = Field("pt-BR", validation_alias="FINPAL_LANGUAGE")



def get_settings():
    env = os.getenv("FINPAL_ENV", "dev")  # default para dev
    env_file = BASE_DIR / f"{env}.env"
    return Settings(_env_file=env_file, _env_file_encoding='utf-8')

settings = get_settings()