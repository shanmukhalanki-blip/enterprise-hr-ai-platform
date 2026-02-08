import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a professional HR assistant.
Your task is to politely rephrase the given HR response.
Do NOT add new information.
Do NOT change numbers or facts.
Keep it concise and professional.
"""

def polish_response(raw_reply: str) -> str:
    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=f"""
{SYSTEM_PROMPT}

Raw HR response:
"{raw_reply}"
"""
        )

        return response.output[0].content[0].text.strip()

    except Exception as e:
        # AI failure should NEVER break HR system
        print("⚠️ AI formatting failed:", repr(e))
        return raw_reply
