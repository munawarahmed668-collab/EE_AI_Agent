def calculate_current(voltage, resistance):
    """Calculate current using Ohm's Law: I = V / R"""
    try:
        voltage = float(voltage)
        resistance = float(resistance)

        if resistance == 0:
            return "❌ Resistance cannot be zero."

        current = voltage / resistance
        return f"{current:.2f} A"

    except Exception:
        return "❌ Invalid input."


def calculate_voltage(current, resistance):
    """Calculate voltage using Ohm's Law: V = I × R"""
    try:
        current = float(current)
        resistance = float(resistance)

        voltage = current * resistance
        return f"{voltage:.2f} V"

    except Exception:
        return "❌ Invalid input."


def calculate_power(voltage, current):
    """Calculate electrical power: P = V × I"""
    try:
        voltage = float(voltage)
        current = float(current)

        power = voltage * current
        return f"{power:.2f} W"

    except Exception:
        return "❌ Invalid input."


def calculate_resistance(voltage, current):
    """Calculate resistance: R = V / I"""
    try:
        voltage = float(voltage)
        current = float(current)

        if current == 0:
            return "❌ Current cannot be zero."

        resistance = voltage / current
        return f"{resistance:.2f} Ω"

    except Exception:
        return "❌ Invalid input."


def calculate_energy(power, time):
    """Calculate energy: E = P × t"""
    try:
        power = float(power)
        time = float(time)

        energy = power * time
        return f"{energy:.2f} Wh"

    except Exception:
        return "❌ Invalid input."


def calculate_series_resistance(*resistors):
    """Calculate total resistance in series"""
    try:
        values = [float(r) for r in resistors]
        total = sum(values)
        return f"{total:.2f} Ω"

    except Exception:
        return "❌ Invalid input."


def calculate_parallel_resistance(*resistors):
    """Calculate total resistance in parallel"""
    try:
        values = [float(r) for r in resistors]

        reciprocal = sum(1 / r for r in values if r != 0)

        if reciprocal == 0:
            return "❌ Invalid resistor values."

        total = 1 / reciprocal
        return f"{total:.2f} Ω"

    except Exception:
        return "❌ Invalid input."