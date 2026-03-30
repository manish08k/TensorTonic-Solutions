import numpy as np
def remove_stopwords(tokens, stopwords):
    tokens=np.array(tokens)
    stopwords=np.array(stopwords)
    a=[]
    for i in tokens:
        if i not in stopwords:
            a.append(i)
    return a
        
