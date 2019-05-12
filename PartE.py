import numpy as np


def m(t):
    return np.sin(5*np.pi*t) / (np.pi * t)


def r(t):
    return m(t)*np.cos(30*np.pi*t)
