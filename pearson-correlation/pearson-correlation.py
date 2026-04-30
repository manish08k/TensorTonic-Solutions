import numpy as np

def pearson_correlation(X):  # ✅ renamed
    # Convert list to numpy array if needed
    X = np.array(X)
    
    # Check validity
    if X.ndim != 2 or X.shape[0] < 2:
        return None
    
    # Step 1: Mean center
    X_centered = X - np.mean(X, axis=0)
    
    # Step 2: Covariance matrix
    cov = (X_centered.T @ X_centered) / (X.shape[0] - 1)
    
    # Step 3: Standard deviations
    std = np.sqrt(np.diag(cov))
    
    # Step 4: Outer product
    denom = np.outer(std, std)
    
    # Step 5: Correlation matrix
    corr = cov / denom
    
    # Step 6: Handle zero variance
    corr[denom == 0] = np.nan
    
    return corr