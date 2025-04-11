import numpy as np
import TimeSeries as ts

def main():
    # Create time vector (100 elements from 0 to 1)
    vector = np.linspace(0, 3, 200)
    f_x = np.cos(vector)
    print(ts.integral(vector, f_x))

    noisy_function = ts.create_noisy_time_series(vector)
    ts.plot(vector, noisy_function)
    print(ts.integral(vector, np.cos(vector)))

main()