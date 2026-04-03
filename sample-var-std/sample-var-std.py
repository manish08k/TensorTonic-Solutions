def sample_var_std(x):
    """
    Compute unbiased sample variance and standard deviation.
    """
    import math
    
    n = len(x)
    if n < 2:
        raise ValueError("At least 2 data points required")
    
    mean = sum(x) / n
    
    sq_diff = sum((xi - mean) ** 2 for xi in x)
    
    var = sq_diff / (n - 1)   # Bessel correction
    std = math.sqrt(var)
    
    return (var, std)