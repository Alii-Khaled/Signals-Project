import numpy as np


def rect(t):
    y = (np.sign(t + 0.5) - np.sign(t - 0.5)) > 0
    return y


def triangle(t):
    y = (1 - abs(t))*(t >= -1)*(t <= 1)
    return y


def uStep(t):
    # Unit Step Function.
    y = (t >= 0)*1
    return y


def rTriangle(t):
    # Triangle of Base 6 units from -3 to 3 & Height of 2 units.
    y = (2 - (2/3) * abs(t))*(t >= -3)*(t <= 3)
    return y


def signal(t):
    x = np.exp(-3*t) * np.sin(8*np.pi/5 * t) * uStep(t + 2)
    return x
