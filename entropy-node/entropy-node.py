import numpy as np

def entropy_node(y):
    y=np.array(y)
    vals,counts = np.unique(y,return_counts=True)
    p = counts/len(y)
    a=-np.sum(p*np.log2(p))
    return a