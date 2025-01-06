import requests
import json
import os
#from dotenv import load_dotenv
from tinydb import TinyDB
import pprint
from datetime import datetime
#pip install python-dotenv

def extract():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    return response.json()["data"]


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

def salvar_dados_tiny_db(dados, db_name = "bitcoin.json"):
    db = TinyDB(db_name)
    db.insert(dados)
    print("Dados salvos com sucesso!")

if __name__ == "__main__":
    dados_json = extract()
    dados_tratados = transform(dados_json)
    salvar_dados_tiny_db(dados_tratados)
    #print(dados_tratados)