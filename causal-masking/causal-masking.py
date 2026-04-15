import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    scores = np.asarray(scores, dtype=float)
    T = scores.shape[-1]
    
    mask = np.triu(np.ones((T, T), dtype=bool), k=1)
    
    masked = scores.copy()
    masked[..., mask] = mask_value
    
    return masked