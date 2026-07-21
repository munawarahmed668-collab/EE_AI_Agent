import re

from ai.chatbot import ask_gemini
from ai.memory import ChatMemory
from ai.rag import search_pdf

from tools.calculators import (
    calculate_current,
    calculate_voltage,
    calculate_power,
    calculate_resistance,
    calculate_energy,
)

memory = ChatMemory()


def extract_numbers(text):
    """Extract all numbers from user input."""
    return [float(n) for n in re.findall(r"\d+\.?\d*", text)]


def process_question(question):

    lower = question.lower()
    numbers = extract_numbers(question)

    # ------------------------
    # Current
    # ------------------------
    if "current" in lower and len(numbers) >= 2:
        answer = calculate_current(numbers[0], numbers[1])

        memory.add("User", question)
        memory.add("Assistant", answer)
        return answer

    # ------------------------
    # Voltage
    # ------------------------
    if "voltage" in lower and len(numbers) >= 2:
        answer = calculate_voltage(numbers[0], numbers[1])

        memory.add("User", question)
        memory.add("Assistant", answer)
        return answer

    # ------------------------
    # Power
    # ------------------------
    if "power" in lower and len(numbers) >= 2:
        answer = calculate_power(numbers[0], numbers[1])

        memory.add("User", question)
        memory.add("Assistant", answer)
        return answer

    # ------------------------
    # Resistance
    # ------------------------
    if "resistance" in lower and len(numbers) >= 2:
        answer = calculate_resistance(numbers[0], numbers[1])

        memory.add("User", question)
        memory.add("Assistant", answer)
        return answer

    # ------------------------
    # Energy
    # ------------------------
    if "energy" in lower and len(numbers) >= 2:
        answer = calculate_energy(numbers[0], numbers[1])

        memory.add("User", question)
        memory.add("Assistant", answer)
        return answer

    # ------------------------
    # Search PDF
    # ------------------------
    try:
        context = search_pdf(question)
    except Exception:
        context = ""

    # ------------------------
    # Chat History
    # ------------------------
    history = memory.get_context()

    # ------------------------
    # Gemini
    # ------------------------
    answer = ask_gemini(
        question=question,
        context=context,
        memory=history,
    )

    memory.add("User", question)
    memory.add("Assistant", answer)

    return answer