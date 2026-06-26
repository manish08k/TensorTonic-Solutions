def item_cf_predict(user_ratings, item_similarities, target):
    """
    Predict the rating using item-based collaborative filtering.
    """
    weighted_sum = 0.0
    total_weight = 0.0

    for i in range(len(user_ratings)):
        if i == target:
            continue
        if item_similarities[i] > 0 and user_ratings[i] != 0:
            weighted_sum += item_similarities[i] * user_ratings[i]
            total_weight += item_similarities[i]

    if total_weight == 0:
        return 0.0

    return weighted_sum / total_weight