import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

data = {
    "model": "llama-3.1-8b-instant",
    "messages": [{"role": "user", "content": "Hola, dame una receta simple"}],
}

r = requests.post(url, json=data, headers=headers)

print("STATUS:", r.status_code)
print("BODY:", r.text)
