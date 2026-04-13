import numpy as np

def dice_loss(p, y, eps=1e-8):
    p = np.array(p).astype(float)
    y = np.array(y).astype(float)
    
    intersection = np.sum(p * y)
    union = np.sum(p) + np.sum(y)
    
    dice = (2 * intersection + eps) / (union + eps)
    return 1 - dice