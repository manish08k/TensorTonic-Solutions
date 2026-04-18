import numpy as np

def covariance_matrix(X):
    # Convert to numpy array
    X = np.array(X)
    
    # Validate input
    if X.ndim != 2 or X.shape[0] < 2:
        return None
    
    N = X.shape[0]
    
    # Step 1: Mean
    mu = np.mean(X, axis=0)
    
    # Step 2: Center data
    X_centered = X - mu
    
    # Step 3: Covariance matrix
    cov = (X_centered.T @ X_centered) / (N - 1)
    
    return cov