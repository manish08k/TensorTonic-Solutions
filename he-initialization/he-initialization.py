import numpy as np

def he_initialization(W, fan_in):
    W = np.array(W, dtype=float)
    limit = np.sqrt(6 / fan_in)
    return (W * 2 * limit - limit).tolist()