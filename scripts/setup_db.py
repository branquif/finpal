#!/usr/bin/env python3
import os
import sqlite3
from pathlib import Path

from finpal import config

def setup_database():
    """Configura o banco de dados SQLite inicial."""
    # Garante que o diretório data existe
    db_path = Path(config.DB_PATH)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Verifica se o banco já existe
    if db_path.exists():
        print(f"Banco de dados já existe em {db_path}")
        return
    
    # Cria o banco de dados e as tabelas iniciais
    print(f"Criando banco de dados em {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Habilita chaves estrangeiras
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    # Cria tabelas básicas (apenas para demonstração)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS schema_table_comments (
        table_name TEXT PRIMARY KEY,
        comment TEXT NOT NULL
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS schema_column_comments (
        table_name TEXT NOT NULL,
        column_name TEXT NOT NULL,
        comment TEXT NOT NULL,
        PRIMARY KEY (table_name, column_name)
    );
    """)
    
    # Insere comentário para demonstração
    cursor.execute("""
    INSERT INTO schema_table_comments VALUES 
    ('schema_table_comments', 'Armazena comentários para cada tabela do sistema, sendo parte da documentação auto-contida');
    """)
    
    conn.commit()
    conn.close()
    
    print("Banco de dados inicial criado com sucesso!")

if __name__ == "__main__":
    setup_database()
