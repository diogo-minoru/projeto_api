import requests
import time
from datetime import datetime
from dotenv import load_dotenv
from database import Base, BitcoinPreco
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Monta a URL de conexão ao banco PostgreSQL (sem ?sslmode=...)
DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# Cria o engine e a sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def criar_tabela():
    """Cria a tabela no banco de dados, se não existir."""
    Base.metadata.create_all(engine)
    print("Tabela criada/verificada com sucesso!")

def extract():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    return response.json()["data"]

load_dotenv()

def transform(dados):
    valor = dados["amount"]
    criptomoeda = dados["base"]
    moeda = dados["currency"]
    timestamp = datetime.now().timestamp()

    dados_transformados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": timestamp
    }

    return dados_transformados
"""
def salvar_dados_tiny_db(dados, db_name = "bitcoin.json"):
    db = TinyDB(db_name)
    db.insert(dados)
    print("Dados salvos com sucesso!")
"""
if __name__ == "__main__":
    while True:
        dados_json = extract()
        dados_tratados = transform(dados_json)
        salvar_dados_tiny_db(dados_tratados)
        time.sleep(15)