# Projeto ETL: Extração, Transformação e Carregamento com Python e Requests

## Visão Geral do Projeto
Este projeto demonstra um pipeline ETL (Extração, Transformação, Carregamento) implementado em Python usando a biblioteca `requests`. O pipeline busca dados de uma API, processa-os e carrega os dados transformados em um destino, como um arquivo CSV ou um banco de dados.

## Funcionalidades
- **Extração de Dados**: Recupera dados em formato JSON de uma API pública ou privada usando `requests`.
- **Transformação de Dados**: Limpa, filtra e estrutura os dados para atender aos requisitos específicos.
- **Carregamento de Dados**: Salva os dados transformados em um arquivo CSV ou banco de dados para análise posterior.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/etl-python-requests.git
   cd etl-python-requests
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate # No Windows: venv\Scripts\activate
   ```

3. Instale os pacotes necessários:
   ```bash
   pip install -r requirements.txt
   ```

## Estrutura do Projeto
```
.
├── config.py             # Arquivo de configuração para detalhes e ajustes da API
├── etl.py                # Script principal para executar o pipeline ETL
├── requirements.txt      # Dependências Python
├── README.md             # Documentação do projeto
├── output/               # Diretório para arquivos de saída
└── utils.py              # Funções utilitárias para transformação e carregamento
```

## Exemplo de Configuração
Aqui está um exemplo do arquivo `config.py`:
```python
API_ENDPOINT = "https://api.exemplo.com/dados"
HEADERS = {
    "Authorization": "Bearer SEU_TOKEN_API",
    "Content-Type": "application/json"
}
OUTPUT_FILE = "output/dados_transformados.csv"
```

## Exemplo de Saída
Exemplo de dados transformados salvos como um arquivo CSV:
```
id,nome,idade,cidade
1,João Silva,29,São Paulo
2,Maria Oliveira,34,Rio de Janeiro
```
