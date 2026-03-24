import numpy as np

def mc_policy_evaluation(episodes, gamma, n_states):
    V = np.zeros(n_states)
    S = np.zeros(n_states)
    C = np.zeros(n_states)

    for ep in episodes:
        first = {}
        for i, (s, _) in enumerate(ep):
            if s not in first:
                first[s] = i

        G = 0
        returns = [0]*len(ep)

        for t in reversed(range(len(ep))):
            s, r = ep[t]
            G = r + gamma * G
            returns[t] = G

        for s, t in first.items():
            S[s] += returns[t]
            C[s] += 1

    mask = C > 0
    V[mask] = S[mask] / C[mask]
    return V