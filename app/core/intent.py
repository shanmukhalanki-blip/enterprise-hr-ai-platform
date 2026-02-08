import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

INTENTS = [
    "leave_balance",
    "apply_leave",
    "hr_policy",
    "holiday_list",
    "manager_info",
    "raise_ticket",
    "general_chat"
]

def detect_intent(message: str) -> str:
    prompt = f"""
Classify the employee message into ONE of these intents:
{INTENTS}

Message: "{message}"

Return ONLY the intent name.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    # ✅ SAFE extraction
    text = response.output[0].content[0].text.strip()

    return text if text in INTENTS else "general_chat"
