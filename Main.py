import TimeSeries as ts
import Integral as integral

def main():
    vector = ts.CreateVector()
    noisy_function = ts.CreateNoisyTimeSeries(vector)
    ts.plot(vector, noisy_function)

main()