import os
from openai import OpenAI
from app.core.prompts import SYSTEM_PROMPT

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_reply(context: str, user_message: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
{SYSTEM_PROMPT}

Context:
{context}

User message:
{user_message}
"""
    )

    # ✅ SAFE extraction
    return response.output[0].content[0].text.strip()
