import numpy as np
from matplotlib import pyplot as plt


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

# Cosine basis
def cosine_basis(n, t):
    return np.cos(n * t)

# Polynomial-exponential basis
def poly_exp_basis(n, t):
    return (t**n) * np.exp(n *t)

def integral(x, f_x):
    # Vector that starts at 0 and ends at 1 with increments of 0.01
    #x = np.arange(0, 1.01, 0.01)

    # Initialize sum
    s = 0

    # Add every trapezoid
    for i in range(1, len(x)):
        height = (f_x[i] + f_x[i-1]) / 2
        base = x[i] - x[i-1]
        s += height * base

    # Return the result
    return s


def inner_product(f_x, g_x, t):
    return integral(f_x * g_x, t)