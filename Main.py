import numpy as np
import TimeSeries as ts

def main():
    # Create time vector (300 elements from 0 to 3)
    vector = np.linspace(0, 3, 300)

    noisy_function = ts.create_noisy_time_series(vector)
    basis_function = ts.create_basis_function(5, vector)
    ts.plot(vector, noisy_function)
    ts.plot(vector, basis_function)

main()