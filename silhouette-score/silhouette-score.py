import numpy as np

def silhouette_score(X, labels):
    X, labels = np.array(X), np.array(labels)
    D = np.linalg.norm(X[:, None] - X[None, :], axis=2)
    S = []

    for i in range(len(X)):
        same = labels == labels[i]
        other = labels != labels[i]

        a = D[i, same].sum() / max(same.sum() - 1, 1)
        b = min(D[i, labels == l].mean() for l in set(labels) if l != labels[i])

        S.append((b - a) / max(a, b) if max(a, b) > 0 else 0)

    return float(np.mean(S))