import numpy as np


def sigmoid(x):
    x = np.where(x >= 10, 10, x)
    x = np.where(x <= -10, -10, x)
    return (1 - np.exp(-2 * x)) / (1 + np.exp(-2 * x))


print(sigmoid(-5))
