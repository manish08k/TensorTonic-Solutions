def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    result = values[:]
    n = len(result)

    i = 0
    while i < n:
        if result[i] is not None:
            i += 1
            continue

        left = i - 1
        j = i
        while result[j] is None:
            j += 1
        right = j

        left_val = result[left]
        right_val = result[right]
        gap = right - left

        for k in range(left + 1, right):
            result[k] = left_val + (k - left) * (right_val - left_val) / gap

        i = right

    return result