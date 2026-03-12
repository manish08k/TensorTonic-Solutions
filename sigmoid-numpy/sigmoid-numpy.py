import numpy as np

def sigmoid(x):
    x = np.clip(x, -250, 250)
    return 1 / (1 + np.exp(-x))