import math

def ndcg(relevance_scores, k):
    """
    Compute NDCG@k.
    """

    k = min(k, len(relevance_scores))

    def dcg(scores):
        total = 0.0

        for i in range(k):
            rel = scores[i]

            gain = (2 ** rel) - 1
            discount = math.log2(i + 2)

            total += gain / discount

        return total

    # Actual DCG
    dcg_score = dcg(relevance_scores)

    # Ideal DCG
    ideal_scores = sorted(relevance_scores, reverse=True)
    idcg_score = dcg(ideal_scores)

    # Avoid division by zero
    if idcg_score == 0:
        return 0.0

    return dcg_score / idcg_score