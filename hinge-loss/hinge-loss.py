import numpy as np

def hinge_loss(y_true, y_score, margin=1, reduction="mean"):
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)

    if y_true.shape != y_score.shape:
        raise ValueError("Shape mismatch")
    if not np.all(np.isin(y_true, [-1, 1])):
        raise ValueError("Labels must be -1 or 1")

    loss = np.maximum(0, margin - y_true * y_score)

    return float(np.mean(loss)) if reduction == "mean" else float(np.sum(loss))