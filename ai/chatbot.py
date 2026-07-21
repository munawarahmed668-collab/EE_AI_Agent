from google import genai
from config import GEMINI_API_KEY, CHAT_MODEL

client = genai.Client(
    api_key=GEMINI_API_KEY
)

SYSTEM_PROMPT = """
You are an Electrical Engineering AI Assistant.

You help students understand electrical engineering concepts.

Always:
- Explain clearly.
- Show formulas.
- Solve problems step by step.
- If PDF context is available, use it first.
- If there is no PDF context, answer using your own knowledge.
"""

def ask_gemini(question, context="", memory=""):

    prompt = f"""
{SYSTEM_PROMPT}

==============================
Conversation History
==============================
{memory}

==============================
Reference Context
==============================
{context}

==============================
Current Question
==============================
{question}
"""

    response = client.models.generate_content(
        model=CHAT_MODEL,
        contents=prompt
    )

    return response.text