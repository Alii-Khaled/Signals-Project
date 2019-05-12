import numpy as np
import math


def h(t):
    t = t % 6
    signal = (1 - 2*np.abs(6 - t)) * (t >= 5.5) + (1 - 2*np.abs(t)) * (t <= 0.5)

    return signal


def fourierSeries(period, N):

    result = []
    T = len(period)
    t = np.arange(T)
    for n in range(-N, N+1):
        an = 2/T*(period * np.cos(2*np.pi*n*t/T)).sum()
        bn = 2/T*(period * np.sin(2*np.pi*n*t/T)).sum()
        result.append((an, bn))
    return np.array(result)
