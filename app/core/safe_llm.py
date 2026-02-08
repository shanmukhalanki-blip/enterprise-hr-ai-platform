import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(prompt: str) -> str:
    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt
        )

        return response.output[0].content[0].text.strip()

    except Exception as e:
        print("⚠️ OpenAI error:", repr(e))
        return "I’m temporarily unable to answer. Please try again later."
