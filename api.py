import requests
import json
import os
from dotenv import load_dotenv
#pip install python-dotenv
url = "https://api.openai.com/v1/chat/completions"

open_ai_key = os.getenv("key")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {open_ai_key}"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Qual a capital do brasil?"}]
}

response = requests.post(url = url, headers = headers, data = json.dumps(data))

print(response.json())