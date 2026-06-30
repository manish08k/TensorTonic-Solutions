def user_based_cf_prediction(similarities, ratings):
    """
    Predict a rating using user-based collaborative filtering.
    """
    weighted_sum = 0.0
    total_similarity = 0.0

    for sim, rating in zip(similarities, ratings):
        if sim > 0:
            weighted_sum += sim * rating
            total_similarity += sim

    if total_similarity == 0:
        return 0.0

    return weighted_sum / total_similarity