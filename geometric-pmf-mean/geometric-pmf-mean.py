import numpy as np

def geometric_pmf_mean(k, p):
    k = np.array(k)
    
    # PMF formula
    pmf = (1 - p) ** (k - 1) * p
    
    # Mean
    mean = 1 / p
    
    return pmf, float(mean)