import numpy as np

def dropout(x, p=0.5, rng=None):
    x = np.array(x)  

    if not 0 <= p < 1:
        raise ValueError("p must be in [0, 1)")

    random_func = rng.random if rng is not None else np.random.random

    mask = random_func(x.shape) >= p
    scale = 1.0 / (1.0 - p) if p < 1 else 0.0

    output = x * mask * scale
    dropout_pattern = mask.astype(x.dtype) * scale

    return output, dropout_pattern