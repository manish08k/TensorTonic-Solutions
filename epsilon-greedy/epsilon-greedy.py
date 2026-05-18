import numpy as np

def epsilon_greedy(q_values, epsilon, rng=None):
    """
    Select an action using ε-greedy policy.

    Parameters:
    q_values : np.ndarray
        1D array of Q-values for current state.
    epsilon : float
        Exploration probability in [0, 1].
    rng : np.random.Generator, optional
        Random number generator for deterministic testing.

    Returns:
    int
        Selected action index.
    """
    
    if rng is None:
        rng = np.random

    n_actions = len(q_values)

    # Explore
    if rng.random() < epsilon:
        return int(rng.integers(n_actions) if hasattr(rng, "integers")
                   else rng.randint(n_actions))

    # Exploit
    return int(np.argmax(q_values))