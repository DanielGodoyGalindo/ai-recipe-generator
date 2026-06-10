import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


def generate_recipe(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
    }

    response = requests.post(GROQ_URL, json=data, headers=headers)
    print("Status:", response.status_code)
    print("Body:", response.text)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
