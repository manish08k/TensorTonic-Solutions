def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """

    n = len(y_true)

    # Store values for each bin
    bins = [[] for _ in range(n_bins)]

    # Assign predictions to bins
    for y, p in zip(y_true, y_pred):

        # Handle p == 1.0 edge case
        if p == 1.0:
            bin_idx = n_bins - 1
        else:
            bin_idx = int(p * n_bins)

        bins[bin_idx].append((y, p))

    ece = 0.0

    # Compute ECE
    for b in bins:
        if not b:
            continue

        bin_size = len(b)

        acc = sum(y for y, _ in b) / bin_size
        conf = sum(p for _, p in b) / bin_size

        ece += (bin_size / n) * abs(acc - conf)

    return ece