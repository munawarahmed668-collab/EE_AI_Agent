import numpy as np
import matplotlib.pyplot as plt


def plot_sine_wave(amplitude=1, frequency=50):
    t = np.linspace(0, 0.1, 1000)
    y = amplitude * np.sin(2 * np.pi * frequency * t)

    plt.figure(figsize=(8, 4))
    plt.plot(t, y)
    plt.title("Sine Wave")
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage")
    plt.grid(True)

    filename = "sine_wave.png"
    plt.savefig(filename)
    plt.close()

    return filename