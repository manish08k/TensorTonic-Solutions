import numpy as np

def contrastive_loss(a, b, y, margin=1.0, reduction="mean"):
    a = np.asarray(a, dtype=np.float32)
    b = np.asarray(b, dtype=np.float32)
    y = np.asarray(y, dtype=np.float32)

    if a.ndim == 1:
        a = a[None, :]
    if b.ndim == 1:
        b = b[None, :]

    if a.shape != b.shape:
        raise ValueError("a and b must have the same shape")

    if y.ndim == 0:
        y = np.array([y], dtype=np.float32)

    if not np.all((y == 0) | (y == 1)):
        raise ValueError("y must contain only 0 or 1")

    diff = a - b
    d = np.linalg.norm(diff, axis=1)

    loss = y * (d ** 2) + (1 - y) * np.maximum(0, margin - d) ** 2

    if reduction == "mean":
        return float(np.mean(loss))   
    elif reduction == "sum":
        return float(np.sum(loss))
    else:
        raise ValueError("reduction must be 'mean' or 'sum'")