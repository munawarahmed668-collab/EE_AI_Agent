from google import genai
from PIL import Image

from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def analyze_circuit(image_path, question):
    """
    Analyze an electrical circuit image using Gemini Vision.
    """

    try:
        image = Image.open(image_path)

        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=[
                image,
                f"""
You are an expert Electrical Engineering professor.

Analyze the uploaded circuit image carefully.

Your response should include:

1. Components present
2. Circuit type
3. How the circuit works
4. Current flow
5. Voltage explanation
6. Any equations used
7. Safety notes if applicable

Student Question:
{question}

Explain step by step.
"""
            ]
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"