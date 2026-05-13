import numpy as np

def _entropy(y):
    """
    Helper: Compute Shannon entropy (base 2) for labels y.
    """
    y = np.asarray(y)
    if y.size == 0:
        return 0.0
    vals, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum()) if p.size else 0.0

def information_gain(y, split_mask):
    """
    Compute Information Gain of a binary split on labels y.
    Use the _entropy() helper above.
    """
    y = np.asarray(y)
    split_mask = np.asarray(split_mask, dtype=bool)

    # Split into left and right groups
    y_left = y[split_mask]
    y_right = y[~split_mask]

    n = len(y)
    n_left = len(y_left)
    n_right = len(y_right)

    # Edge case: one side empty
    if n_left == 0 or n_right == 0:
        return 0.0

    # Parent entropy
    parent_entropy = _entropy(y)

    # Weighted child entropy
    weighted_entropy = (
        (n_left / n) * _entropy(y_left) +
        (n_right / n) * _entropy(y_right)
    )

    # Information Gain
    return float(parent_entropy - weighted_entropy)