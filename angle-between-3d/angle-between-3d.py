import numpy as np

def angle_between_3d(v, w):
    """
    Compute angle (in radians) between two 3D vectors.

    Parameters:
    v, w : array-like of shape (3,)

    Returns:
    float
        Angle in radians in [0, pi].
        Returns np.nan if either vector is zero.
    """

    v = np.asarray(v, dtype=float)
    w = np.asarray(w, dtype=float)

    # Compute vector norms
    norm_v = np.linalg.norm(v)
    norm_w = np.linalg.norm(w)

    # Handle zero vectors
    if norm_v == 0 or norm_w == 0:
        return np.nan

    # Compute cosine of angle
    cos_theta = np.dot(v, w) / (norm_v * norm_w)

    # Clamp due to floating-point precision
    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    # Return angle
    return float(np.arccos(cos_theta))