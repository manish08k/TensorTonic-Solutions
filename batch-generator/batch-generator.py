import numpy as np

def batch_generator(X, y, batch_size, rng=None, drop_last=False):
    # Convert inputs to NumPy arrays
    X = np.asarray(X)
    y = np.asarray(y)

    # Validate batch size
    if batch_size <= 0:
        raise ValueError("batch_size must be > 0")

    # Validate matching lengths
    if len(X) != len(y):
        raise ValueError("X and y must have the same length")

    n = len(X)

    # Create RNG if not provided
    if rng is None:
        rng = np.random.default_rng()

    # Shuffle indices
    indices = rng.permutation(n)

    # Apply same shuffle to X and y
    X_shuffled = X[indices]
    y_shuffled = y[indices]

    # Yield mini-batches
    for start in range(0, n, batch_size):
        end = start + batch_size

        # Drop incomplete last batch if requested
        if drop_last and end > n:
            break

        yield X_shuffled[start:end], y_shuffled[start:end]