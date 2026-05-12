import numpy as np

def knn_distance(X_train, X_test, k):
    """
    Compute pairwise distances and return k nearest neighbor indices.
    """

    # Convert to numpy arrays
    X_train = np.array(X_train)
    X_test = np.array(X_test)

    # Handle 1D inputs
    if X_train.ndim == 1:
        X_train = X_train.reshape(-1, 1)

    if X_test.ndim == 1:
        X_test = X_test.reshape(-1, 1)

    n_train = X_train.shape[0]
    n_test = X_test.shape[0]

    # Pairwise Euclidean distances using broadcasting
    distances = np.sqrt(
        np.sum((X_test[:, np.newaxis, :] - X_train[np.newaxis, :, :]) ** 2, axis=2)
    )

    # Number of valid neighbors
    actual_k = min(k, n_train)

    # Get indices of nearest neighbors
    nearest = np.argsort(distances, axis=1)[:, :actual_k]

    # Pad with -1 if k > n_train
    if k > n_train:
        padding = -1 * np.ones((n_test, k - n_train), dtype=int)
        nearest = np.hstack((nearest, padding))

    return nearest.astype(int)