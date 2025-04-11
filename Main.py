import numpy as np
import TimeSeries as ts
import Integral as 

def main():
    # Create time vector (300 elements from 0 to 3)
    vector = np.linspace(0, 3, 300)

    noisy_function = ts.create_noisy_time_series(vector)
    ts.plot(vector, noisy_function)

main()