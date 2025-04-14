import numpy as np

# Create a time series with noise and takes a vector as parameter
def create_noisy_time_series(t):
    # Generate a smooth function
    f_t = t**2

    # Add noise
    noise = 1.0 * np.random.randn(len(t))
    noisy_time_series = f_t + noise

    return noisy_time_series

# Compute an integral given a vector (x values) and a function (f of x values)
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

# Polynomial basis
def polynomial_basis(n, t):
    basis = []

    for i in range(0, n):
        function = t**i
        basis.append(function)

    # Return an array of basis functions
    return basis

# Cosine basis
def cosine_basis(n, t):
    basis = []

    for i in range(0, n):
        function = np.cos(t*i)
        basis.append(function)

    # Return an array of basis functions
    return basis


# Formulates a linear system and aproximates the function of the noisy time series using the sum of coefficients and basis functions
def approximate_function(coeff, basis):
    approx = 0;
    for i in range(0, len(basis)):
        approx += (coeff[i] * basis[i])

    # Return the approximated function
    return approx