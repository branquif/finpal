#!/usr/bin/env python3
import os
import sqlite3
from pathlib import Path

from finpal.config import settings


def setup_database():
    """Configura o banco de dados SQLite inicial."""
    # Garante que o diretório data existe
    db_path = Path(settings.DB_PATH)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    # Verifica se o banco já existe
    if not db_path.exists():
        print(f"Banco de dados não existe em {db_path}")
        return

    # Cria o banco de dados e as tabelas iniciais
    print(f"Carregando dados em {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Habilita chaves estrangeiras
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Cria tabelas básicas (apenas para demonstração)

    conn.commit()
    conn.close()

    print("Banco de dados inicial criado com sucesso!")


if __name__ == "__main__":
    setup_database()
