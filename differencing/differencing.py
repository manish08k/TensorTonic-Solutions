def differencing(series, order):
    r=series[:]
    for _ in range(order):
        r=[r[i]-r[i-1] for i in range(1,len(r))] 
    return r