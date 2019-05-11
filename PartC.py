import numpy as np
from PartA import uStep


def z(t):
    t = t % 6
    signal = np.exp(-1*np.abs(t)/3) * np.sin(4*np.pi*t) * (uStep(t) - uStep(t - 5))
    return signal


def EnergyZ():
    rng = np.arange(-99999, 99999, 0.01)
    energy = np.sum(z(rng) ** 2 * 0.01)
    if energy > 9999:
        energy = "Infinity"

    return energy


def PowerZ():
    rng = np.arange(-99999, 99999, 0.01)
    power = np.sum((1/(2 * 99999)) * z(rng)**2 * 0.01)
    if power > 99999:
        power = "Infinity"

    return power
