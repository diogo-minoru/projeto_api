import requests
import time
from datetime import datetime
from dotenv import load_dotenv
from database import Base, BitcoinPreco
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#import logging
#import logfire

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Monta a URL de conexão ao banco PostgreSQL (sem ?sslmode=...)
"""
DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)
"""

"""
logfire.configure()
basicConfig(handlers=[logfire.LogfireLoggingHandler()])
logger = getLogger(__name__)
logger.setlevel(logging.INFO)
logfire.instrument_requests()
logfire.instrument_sqlalchemy()
"""

DATABASE_URL = "postgresql://bancodedados_6sd5_user:KX1htrnJTKV3y83nz74xdiCMvIEl7SU2@dpg-ctuqev9opnds73c8bvm0-a.oregon-postgres.render.com:5432/bancodedados_6sd5"

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
    valor = float(dados["amount"])
    criptomoeda = str(dados["base"])
    moeda = str(dados["currency"])
    timestamp = datetime.now()

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
def salvar_dados_postgres(dados):
    """Salva os dados no banco PostgreSQL."""
    session = Session()
    novo_registro = BitcoinPreco(**dados)
    session.add(novo_registro)
    session.commit()
    session.close()
    print(f"[{dados['timestamp']}] Dados salvos no PostgreSQL!")

if __name__ == "__main__":
    criar_tabela()
    print("Iniciando ETL com atualização a cada 15 segundos... (CTRL+C para interromper)")

    while True:
        try:
            dados_json = extract()
            if dados_json:
                dados_tratados = transform(dados_json)
                print("Dados Tratados:", dados_tratados)
                salvar_dados_postgres(dados_tratados)
            time.sleep(15)
        except KeyboardInterrupt:
            print("\nProcesso interrompido pelo usuário. Finalizando...")
            break
        except Exception as e:
            print(f"Erro durante a execução: {e}")
            time.sleep(15)