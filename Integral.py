import numpy as np

def integral():
    # Vector that starts at 0 and ends at 1 with increments of 0.01
    x = np.arange(0, 1.01, 0.01)

    # Initialize sum
    s = 0

    # Add every trapezoid
    for i in range(1, len(x)):
        height = (x[i]**2 + x[i-1]**2) / 2
        base = x[i] - x[i-1]
        s += height * base

    # Return the result
    return s

# TODO
def InnerProduct():
    pass