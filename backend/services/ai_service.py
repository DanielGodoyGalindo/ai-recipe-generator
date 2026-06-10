import os
import requests

API_KEY = os.getenv("OPENROUTER_API_KEY")

print("API KEY EXISTS:", API_KEY is not None)
print("API KEY LENGTH:", len(API_KEY) if API_KEY else 0)


def generate_recipe(prompt: str) -> str:
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "meta-llama/llama-3.1-8b-instruct",
            "messages": [{"role": "user", "content": prompt}],
        },
    )
    
    print("Status:", response.status_code)
    print("Body:", response.text)

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
