import numpy as np
from matplotlib import pyplot as plt
import math


def create_noisy_time_series(t):
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

def create_basis_function(n, t):
    np.cos(n * t)