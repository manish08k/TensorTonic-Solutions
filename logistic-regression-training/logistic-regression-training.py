import numpy as np

def _sigmoid(z):
    # Numerically stable sigmoid
    return 1 / (1 + np.exp(-z))

def train_logistic_regression(X, y, lr=0.1, steps=500):
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    N, D = X.shape

    # Initialize parameters
    w = np.zeros(D)
    b = 0.0

    for _ in range(steps):
        # Forward pass
        z = X @ w + b
        p = _sigmoid(z)

        # Gradients
        dz = p - y
        dw = (1 / N) * (X.T @ dz)
        db = (1 / N) * np.sum(dz)

        # Update parameters
        w -= lr * dw
        b -= lr * db

    return w, b