import numpy as np
from PartA import uStep


def y(t):

    signal = np.exp(-np.abs(t)/5.0) * (uStep(t+1) - uStep(t-3))
    return signal


def y1(t):
    return y(2*t)


def y2(t):
    return y(t + 2)


def y3(t):
    return y(4*t - 2)
