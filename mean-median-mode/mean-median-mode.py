import numpy as np
from collections import Counter

def mean_median_mode(x):
    x = np.array(x, dtype=float)
    
    mean = float(np.sum(x) / len(x))
    
    x_sorted = np.sort(x)
    n = len(x)
    
    if n % 2 == 1:
        median = float(x_sorted[n // 2])
    else:
        median = float((x_sorted[n // 2 - 1] + x_sorted[n // 2]) / 2)
    
    freq = Counter(x)
    max_freq = max(freq.values())
    
    modes = [val for val, count in freq.items() if count == max_freq]
    mode = float(min(modes))
    
    return mean, median, mode