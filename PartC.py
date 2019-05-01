import numpy as np
from PartA import uStep


def z(t):
    t = t % 6
    signal = np.exp(-1*np.abs(t)/3) * np.sin(4*np.pi*t) * (uStep(t) - uStep(t - 5))
    return signal

