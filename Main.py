import numpy as np
from matplotlib import pyplot as plt
import TimeSeries as ts

def main():
    # Create vector (200 elements from 0 to 3)
    t = np.linspace(0, 3, 200)
    
    # Create a noisy function
    noisy_function = ts.create_noisy_time_series(t)

    # Create basis fuctions
    basis_functions = ts.cosine_basis(4, t)


    # Linear system
    n = len(basis_functions)
    A = np.zeros((n,n))
    b = np.zeros(n)

    for i in range(n):
        for j in range(n):
            # Create a square matrix of inner products of the basis functions
            A[i, j] = ts.integral(t, basis_functions[i] * basis_functions[j],)
        # Create a vector of the inner product between the basis functions and the noisy function
        b[i] = ts.integral(t, basis_functions[i] * noisy_function)

    # Solve for the cooefficients (x in Ax = b)
    coefficients = np.linalg.solve(A, b)

    # Approximate the new function
    new_function = ts.approximate_function(coefficients, basis_functions)

    # Plot
    plt.figure(figsize=(8,6))
    plt.plot(t, noisy_function, "b", label="Noisy Function")
    plt.plot(t, new_function, "r", label="Polynomial Approximation")
    plt.legend()
    plt.title("Time Series With Noise")
    plt.grid(True)
    plt.show()

main()