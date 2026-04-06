import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    
    Returns:
        pmf (np.ndarray): probabilities
        mean (float): expected value
        var (float): variance
    """
    # Convert input to NumPy array
    x = np.array(x)
    
    # Validate inputs
    if not np.all((x == 0) | (x == 1)):
        raise ValueError("x must contain only 0s and 1s")
    if not (0 <= p <= 1):
        raise ValueError("p must be between 0 and 1")
    
    # Vectorized PMF
    pmf = p**x * (1 - p)**(1 - x)
    
    # Moments
    mean = float(p)
    var = float(p * (1 - p))
    
    return pmf, mean, var