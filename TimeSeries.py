import numpy as np
from matplotlib import pyplot as plt
import math

# Create time vector
t = np.linspace(0, 10, 100)

# Generate a smooth function
f_t = t**2

# Add noise
noise = 10.0 * np.random.randn(len(t))
noisy_time_series = f_t + noise

# Plot
plt.figure(figsize=(8,6))
plt.plot(t, f_t)
plt.plot(t, noisy_time_series, "b")
plt.legend()
plt.title("Time Series With Noise")
plt.grid(True)
plt.show()