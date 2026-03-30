def catalog_coverage(recommendations, n_items):
    a=[]
    for i in recommendations:
        for j in i:
            a.append(j)
    return float(len(set(a))/n_items)
            