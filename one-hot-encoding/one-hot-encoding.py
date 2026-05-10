import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    
    y = np.array(y)
    
    if num_classes is None:
        num_classes = np.max(y) + 1

    # Validate labels
    if np.any(y >= num_classes):
        raise ValueError("Labels must be less than num_classes")

    # Create one-hot matrix
    one_hot_matrix = np.zeros((len(y), num_classes), dtype=float)
    
    # Vectorized assignment
    one_hot_matrix[np.arange(len(y)), y] = 1.0

    return one_hot_matrix