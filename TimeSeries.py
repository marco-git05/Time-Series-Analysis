import numpy as np
from matplotlib import pyplot as plt
import math

# Create time vector (300 elements from 0 to 3)
def CreateVector():
    t = np.linspace(0, 3, 300)
    return t

def CreateNoisyTimeSeries(t):
    # Generate a smooth function
    f_t = t**2

    # Add noise
    noise = 1.0 * np.random.randn(len(t))
    noisy_time_series = f_t + noise

    return noisy_time_series

# Plot
def plot(t, function):
    plt.figure(figsize=(12,10))
    plt.plot(t, function, "b")
    plt.legend()
    plt.title("Time Series With Noise")
    plt.grid(True)
    plt.show()