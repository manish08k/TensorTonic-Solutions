import numpy as np

def log_transform(values):
    """
    Apply log(1 + x) transformation to a list of non-negative values.
    
    Returns:
        List[float]
    """
    # Convert to numpy array
    values = np.array(values)
    
    # Apply log1p (natural log of 1 + x)
    transformed = np.log1p(values)
    
    # Return as Python list
    return transformed.tolist()