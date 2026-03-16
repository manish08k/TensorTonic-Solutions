def priority_replay_sample(priorities, alpha, beta):
    n = len(priorities)

    a = [p**alpha for p in priorities]
    s = sum(a)

    p = [x/s for x in a]
    b = [(n*x)**(-beta) for x in p]

    m = max(b)
    b = [x/m for x in b]

    return [[round(x,4) for x in p], [round(x,4) for x in b]]