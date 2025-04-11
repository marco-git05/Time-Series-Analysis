import numpy as np


# Creates a time series with noise and takes a vector as parameter
def create_noisy_time_series(t):
    # Generate a smooth function
    f_t = t**2

    # Add noise
    noise = 1.0 * np.random.randn(len(t))
    noisy_time_series = f_t + noise

    return noisy_time_series

# Function that computes an integral given a vector (x values) and a function (f of x values)
def integral(x, f_x):
    # Initialize sum
    s = 0

    # Add every trapezoid
    for i in range(1, len(x)):
        height = (f_x[i] + f_x[i-1]) / 2
        base = x[i] - x[i-1]
        s += height * base

    # Return the result
    return s

# Cosine basis
def cosine_basis(n, t):
    return np.cos(n * t)

# Polynomial-exponential basis
def poly_exp_basis(n, t):
    return (t**n) * np.exp(n *t)