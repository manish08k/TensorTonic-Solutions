import numpy as np

def global_avg_pool(x):
    x = np.asarray(x, dtype=float)
    
    if x.ndim == 3:
        return x.mean(axis=(1, 2))
    
    if x.ndim == 4:
        return x.mean(axis=(2, 3))
    
    raise ValueError("Input must be 3D or 4D tensor")