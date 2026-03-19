import numpy as np

def r2_score(y_true, y_pred):
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    
    if np.all(y_true == y_true[0]):
        return 1.0 if np.all(y_true == y_pred) else 0.0
    
    return 1 - np.sum((y_true - y_pred)**2) / np.sum((y_true - np.mean(y_true))**2)