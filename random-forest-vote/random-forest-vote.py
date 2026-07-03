import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    predictions = np.array(predictions)   # (trees, samples)
    n_samples = predictions.shape[1]
    result = []

    for i in range(n_samples):
        votes = predictions[:, i]
        counts = np.bincount(votes)
        result.append(np.argmax(counts))   # smallest label wins on ties

    return result