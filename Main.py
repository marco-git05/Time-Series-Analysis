import numpy as np
from matplotlib import pyplot as plt
import TimeSeries as ts

def main():
    # Create vector (100 elements from 0 to 1)
    t = np.linspace(0, 3, 200)
    
    # Create a noisy function
    noisy_function = ts.create_noisy_time_series(t)

    # Plot
    plt.figure(figsize=(12,10))
    plt.plot(t, noisy_function, "b")
    plt.legend()
    plt.title("Time Series With Noise")
    plt.grid(True)
    plt.show()

main()