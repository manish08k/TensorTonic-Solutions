import numpy as np

def precision_recall_at_k(recommended, relevant, k):
    recommended = np.array(recommended[:k])
    relevant = np.array(relevant)
    inter = np.intersect1d(recommended, relevant)
    a = len(inter) / len(recommended)   
    b = len(inter) / len(relevant)      
    return [a, b]