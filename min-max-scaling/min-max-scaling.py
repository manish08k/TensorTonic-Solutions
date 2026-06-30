def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    rows = len(data)
    cols = len(data[0])

    # Find min and max for each column
    min_vals = [float("inf")] * cols
    max_vals = [float("-inf")] * cols

    for row in data:
        for j in range(cols):
            min_vals[j] = min(min_vals[j], row[j])
            max_vals[j] = max(max_vals[j], row[j])

    # Scale the data
    result = []

    for row in data:
        scaled_row = []
        for j in range(cols):
            if max_vals[j] == min_vals[j]:
                scaled_row.append(0.0)
            else:
                scaled = (row[j] - min_vals[j]) / (max_vals[j] - min_vals[j])
                scaled_row.append(float(scaled))
        result.append(scaled_row)

    return result