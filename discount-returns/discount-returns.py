def discount_returns(rewards, gamma):
    """
    Compute the discounted return at every timestep.
    """
    n = len(rewards)
    G = [0.0] * n
    
    # Base case: last timestep
    G[-1] = float(rewards[-1])
    
    # Fill backwards
    for t in range(n - 2, -1, -1):
        G[t] = rewards[t] + gamma * G[t + 1]
    
    return G