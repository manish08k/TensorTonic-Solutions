import numpy as np
def selu(x):
    x = np.array(x, dtype=float)
    lam = 1.0507009873554805
    alpha = 1.6732632423543772
    return (lam * np.where(x > 0, x, alpha * (np.exp(x) - 1))).tolist()