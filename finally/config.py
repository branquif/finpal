import os
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Ambiente (development, testing, production)
ENV = os.getenv("FINALLY_ENV", "development")

# Caminho do banco de dados
DB_PATH = os.getenv("FINALLY_DB_PATH", str(BASE_DIR / "data" / "finally.db"))

# Chave secreta para tokens e senhas
SECRET_KEY = os.getenv("FINALLY_SECRET_KEY", "chave_secreta_temporaria_para_desenvolvimento")

# Configurações da API
API_HOST = os.getenv("FINALLY_API_HOST", "localhost")
API_PORT = int(os.getenv("FINALLY_API_PORT", "8000"))

# Configurações da aplicação
DEFAULT_CURRENCY = os.getenv("FINALLY_DEFAULT_CURRENCY", "BRL")
DATE_FORMAT = os.getenv("FINALLY_DATE_FORMAT", "DD/MM/YYYY")
LANGUAGE = os.getenv("FINALLY_LANGUAGE", "pt-BR")
