import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    fpr = np.asarray(fpr, dtype=float)
    tpr = np.asarray(tpr, dtype=float)
    
    # Validation
    if fpr.ndim != 1 or tpr.ndim != 1 or len(fpr) != len(tpr) or len(fpr) < 2:
        return None
    
    # Ensure FPR is sorted
    if not np.all(np.diff(fpr) >= 0):
        idx = np.argsort(fpr)
        fpr = fpr[idx]
        tpr = tpr[idx]
    
    # Trapezoidal rule
    delta = np.diff(fpr)
    avg_height = (tpr[:-1] + tpr[1:]) / 2
    
    auc_value = np.sum(delta * avg_height)
    
    return float(auc_value)