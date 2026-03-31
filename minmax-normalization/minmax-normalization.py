import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    X = np.asarray(X, dtype=float)

    # Handle 1D input
    if X.ndim == 1:
        X = X.reshape(-1, 1)

    # Compute min and max along axis
    min_vals = np.min(X, axis=axis, keepdims=True)
    max_vals = np.max(X, axis=axis, keepdims=True)

    # Avoid division by zero using eps
    denom = max_vals - min_vals
    denom = np.where(denom < eps, 1, denom)

    # Scale
    X_scaled = (X - min_vals) / denom

    return X_scaled