import numpy as np

def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    
    Returns:
        float
    """
    # Convert to NumPy arrays
    probs = np.array(prob_distributions)
    tokens = np.array(actual_tokens)
    
    # Validate inputs
    if probs.shape[0] != tokens.shape[0]:
        raise ValueError("Number of distributions must match number of tokens")
    
    # Extract probabilities of actual tokens (vectorized indexing)
    p_i = probs[np.arange(len(tokens)), tokens]
    
    # Avoid log(0) by adding a small epsilon
    eps = 1e-12
    p_i = np.clip(p_i, eps, 1.0)
    
    # Cross-entropy
    H = -np.mean(np.log(p_i))
    
    # Perplexity
    PP = np.exp(H)
    
    return float(PP)