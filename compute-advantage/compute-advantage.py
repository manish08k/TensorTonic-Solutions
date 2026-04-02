import numpy as np

def compute_advantage(states, rewards, V, gamma):
    n = len(rewards)
    G = np.zeros(n)
    A = np.zeros(n)
    
    G[-1] = rewards[-1]
    for t in range(n - 2, -1, -1):
        G[t] = rewards[t] + gamma * G[t + 1]

    for t in range(n):
        A[t] = G[t] - V[states[t]]
    
    return A