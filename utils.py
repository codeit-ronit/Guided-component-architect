import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


def call_llm(system_prompt, user_prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.2
    }

    response = requests.post(GROQ_URL, headers=headers, json=data)

    try:
        response_json = response.json()
    except Exception:
        raise Exception(f"Invalid response from API: {response.text}")

    # 🔥 ADD THIS DEBUG PRINT
    if "choices" not in response_json:
        raise Exception(f"Groq API Error: {response_json}")

    return response_json["choices"][0]["message"]["content"]
