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
    basis = []

    for i in range(1, n):
        basis.append(np.cos(t))

    return basis

# Polynomial-exponential basis
def poly_exp_basis(n, t):
    return (t**n) * np.exp(n *t)

def inner_product(f_x, g_x, t):
    return integral(t, f_x * g_x)

def approximate_function(t, coeff, basis):
    sum = 0;
    for i in range(1, t):
        sum += (coeff * basis)

    return sum
