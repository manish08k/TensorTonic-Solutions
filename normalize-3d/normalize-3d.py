import numpy as np

def normalize_3d(v):
    v = np.asarray(v, dtype=float)

    # Compute norms
    norms = np.linalg.norm(v, axis=-1, keepdims=True)

    # Avoid division by zero
    norms_safe = np.where(norms == 0, 1, norms)

    # Normalize
    v_normalized = v / norms_safe

    # Set zero vectors back to zero
    v_normalized = np.where(norms == 0, 0, v_normalized)

    return v_normalized