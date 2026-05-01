import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    # Convert inputs to numpy arrays
    a = np.array(anchor, dtype=float)
    p = np.array(positive, dtype=float)
    n = np.array(negative, dtype=float)

    # Ensure batch shape (N, D)
    if a.ndim == 1:
        a = a.reshape(1, -1)
        p = p.reshape(1, -1)
        n = n.reshape(1, -1)

    # Squared Euclidean distances
    d_ap = np.sum((a - p) ** 2, axis=1)
    d_an = np.sum((a - n) ** 2, axis=1)

    # Triplet loss
    loss = np.maximum(0, d_ap - d_an + margin)

    # Return mean loss
    return np.mean(loss)