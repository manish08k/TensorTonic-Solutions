def hit_rate_at_k(recommendations, ground_truth, k):
    n = len(recommendations)
    if n == 0:
        return 0.0
    hits = 0
    for recs, truth in zip(recommendations, ground_truth):
        top_k = recs[:k]
        truth_set = set(truth)
        if any(item in truth_set for item in top_k):
            hits += 1
    return hits / n