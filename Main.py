import numpy as np
from matplotlib import pyplot as plt
import TimeSeries as ts

def main():
    # Create vector (100 elements from 0 to 1)
    t = np.linspace(0, 3, 200)
    
    # Create a noisy function
    noisy_function = ts.create_noisy_time_series(t)

    # Create basis fuctions
    basis_functions = ts.cosine_basis(6, t)

    # Linear system
    n = len(basis_functions)
    A = np.zeros((n,n))
    b= np.zeros(n)

    for i in range(n):
        for j in range(n):
            A[i, j] = ts.inner_product(basis_functions[i], basis_functions[j], t)
        b[i] = ts.integral(t, basis_functions[i])
    
    coefficients = np.linalg.solve(A, b)


    new_function = ts.approximate_function(t, coefficients, basis_functions)

    # Plot
    plt.figure(figsize=(12,10))
    plt.plot(t, noisy_function, "b")
    plt.plot(t, new_function, "r")
    plt.legend()
    plt.title("Time Series With Noise")
    plt.grid(True)
    plt.show()

main()