import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute mean Huber loss (vectorized).
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    error = y_true - y_pred
    abs_error = np.abs(error)
    
    # Apply piecewise condition
    quadratic = 0.5 * error**2
    linear = delta * (abs_error - 0.5 * delta)
    
    loss = np.where(abs_error <= delta, quadratic, linear)
    
    return np.mean(loss)