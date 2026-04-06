import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Convert inputs to NumPy arrays
    x = np.array(x)
    y = np.array(y)
    
    # Validate same shape
    if x.shape != y.shape:
        raise ValueError("x and y must have the same shape")
    
    # Vectorized computation
    distance = np.sum(np.abs(x - y))
    
    return float(distance)