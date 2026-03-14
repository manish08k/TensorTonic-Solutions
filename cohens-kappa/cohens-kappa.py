import numpy as np

def cohens_kappa(rater1, rater2):
    r1, r2 = np.array(rater1), np.array(rater2)
    n = len(r1)

    po = np.sum(r1 == r2) / n

    labels = np.union1d(r1, r2)
    pe = sum((np.sum(r1==k)/n) * (np.sum(r2==k)/n) for k in labels)

    return 1.0 if pe == 1 else (po - pe) / (1 - pe)