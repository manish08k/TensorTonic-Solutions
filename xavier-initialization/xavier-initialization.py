import numpy as np

def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    W = np.asarray(W, dtype=float)

    limit = np.sqrt(6.0 / (fan_in + fan_out))

    W_scaled = W * (2 * limit) - limit

    return W_scaled.tolist()