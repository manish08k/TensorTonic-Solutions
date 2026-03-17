def rating_normalization(matrix):
    result=[]
    for i in matrix:
        r=[x for x in i if x!=0]
        m=sum(r)/len(r) if r else 0
        n1=[(x-m) if x!=0 else 0.0 for x in i]
        result.append(n1)
    return result