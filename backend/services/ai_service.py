import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def generate_recipe(prompt: str) -> str:
    
    print("API KEY EXISTS:", OPENROUTER_API_KEY is not None)
    print("API KEY LENGTH:", len(OPENROUTER_API_KEY) if OPENROUTER_API_KEY else 0)
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "nex-agi/nex-n2-pro:free",
        "messages": [{"role": "user", "content": prompt}],
    }

    print("Sending request...")

    response = requests.post(OPENROUTER_URL, headers=headers, json=data, timeout=30)

    print("Status:", response.status_code)
    print("Body:", response.text[:500])

    response.raise_for_status()

    result = response.json()

    return result["choices"][0]["message"]["content"]
