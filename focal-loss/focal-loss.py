import numpy as np

def focal_loss(p, y, gamma=2.0):
    # Convert to numpy arrays
    p = np.array(p, dtype=float)
    y = np.array(y, dtype=float)

    # Small epsilon for numerical stability (avoid log(0))
    eps = 1e-12
    p = np.clip(p, eps, 1 - eps)

    # Compute focal loss (vectorized)
    loss = - (1 - p)**gamma * y * np.log(p) \
           - (p**gamma) * (1 - y) * np.log(1 - p)

    # Return mean loss
    return np.mean(loss)