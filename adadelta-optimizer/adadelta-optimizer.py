import numpy as np

def adadelta_step(w, grad, E_grad_sq, E_update_sq, rho=0.9, eps=1e-6):
    # Convert to float64 for precision
    w = np.asarray(w, dtype=np.float64)
    grad = np.asarray(grad, dtype=np.float64)
    E_grad_sq = np.asarray(E_grad_sq, dtype=np.float64)
    E_update_sq = np.asarray(E_update_sq, dtype=np.float64)
    
    # Step 1: update squared gradient avg
    new_E_grad_sq = rho * E_grad_sq + (1 - rho) * (grad * grad)
    
    # Step 2: compute update (RMS ratio)
    delta_w = - (np.sqrt(E_update_sq + eps) / np.sqrt(new_E_grad_sq + eps)) * grad
    
    # Step 3: update squared update avg
    new_E_update_sq = rho * E_update_sq + (1 - rho) * (delta_w * delta_w)
    
    # Step 4: update parameters
    new_w = w + delta_w
    
    return new_w, new_E_grad_sq, new_E_update_sq