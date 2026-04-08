def target_encoding(categories, targets):
    from collections import defaultdict
    
    sum_dict = defaultdict(float)
    count_dict = defaultdict(int)
    
    for cat, target in zip(categories, targets):
        sum_dict[cat] += target
        count_dict[cat] += 1
    
    mean_dict = {}
    for cat in sum_dict:
        mean_dict[cat] = sum_dict[cat] / count_dict[cat]
    
    return [float(mean_dict[cat]) for cat in categories]