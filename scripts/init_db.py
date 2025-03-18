#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path
import argparse

from finpal.config import settings, get_settings


def init_database(environment=None, force=False):
    """Inicializa o banco de dados SQLite usando Alembic.

    Args:
        environment: O ambiente para inicializar (development, testing, production)
        force: Se True, recria o banco sem perguntar
    """
    # Se um ambiente específico foi solicitado, ajusta as configurações
    if environment:
        os.environ["FINPAL_ENV"] = environment
        # Recarrega as configurações com o novo ambiente
        global settings
        settings = get_settings()

    print(f"Inicializando banco de dados para ambiente: {settings.ENV}")

    # Garante que o diretório data existe
    db_path = Path(settings.DB_PATH)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    # Verifica se o banco já existe
    if db_path.exists():
        print(f"Banco de dados já existe em {db_path}")
        if not force:
            choice = input("Deseja recriar o banco de dados? [s/N]: ")
            if choice.lower() != 's':
                print("Operação cancelada.")
                return
        os.remove(db_path)
        print(f"Banco de dados removido.")

    print(f"Criando banco de dados em {db_path}")

    # Aplica a migração usando Alembic
    try:
        subprocess.run(["alembic", "upgrade", "head"], check=True)
        print(f"Banco de dados {settings.ENV} inicializado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o Alembic: {e}")
        return 1

    # Exibe informações sobre o banco
    print(f"\nResumo do banco de dados ({settings.ENV}):")
    os.system(f'sqlite3 "{db_path}" "SELECT name FROM sqlite_master WHERE type=\'table\' ORDER BY name;"')

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Inicializa o banco de dados FinPal.')
    parser.add_argument('--env', '-e', choices=['development', 'testing', 'production'],
                        help='Ambiente para inicializar')
    parser.add_argument('--force', '-f', action='store_true',
                        help='Força a recriação do banco sem perguntar')
    args = parser.parse_args()

    sys.exit(init_database(args.env, args.force))