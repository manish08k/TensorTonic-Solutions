def max_pooling_2d(X, pool_size):
    """
    Apply 2D max pooling with non-overlapping windows.
    """
    rows = len(X)
    cols = len(X[0])

    out_rows = rows // pool_size
    out_cols = cols // pool_size

    result = []

    for i in range(out_rows):
        row = []
        for j in range(out_cols):
            maximum = float("-inf")

            for r in range(i * pool_size, (i + 1) * pool_size):
                for c in range(j * pool_size, (j + 1) * pool_size):
                    maximum = max(maximum, X[r][c])

            row.append(maximum)
        result.append(row)

    return result