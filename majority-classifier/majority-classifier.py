import numpy as np

def majority_classifier(y_train, X_test):
    y_train = np.asarray(y_train)
    values, counts = np.unique(y_train, return_counts=True)
    max_count = counts.max()
    candidates = set(values[counts == max_count])
    for v in y_train:
        if v in candidates:
            majority = v
            break
    return np.full(len(X_test), majority, dtype=int)