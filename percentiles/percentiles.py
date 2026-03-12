import numpy as np

def percentiles(x, q):
    x=np.array(x)
    q=np.array(q)
    x=np.sort(x)
    c=np.percentile(x,q,method="linear")
    return np.array(c)