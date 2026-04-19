def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    assert len(y_true) == len(y_pred)
    n = len(y_true)

    classes = set(y_true) | set(y_pred)

    # Initialize counts
    tp = {c: 0 for c in classes}
    fp = {c: 0 for c in classes}
    fn = {c: 0 for c in classes}
    support = {c: 0 for c in classes}

    # Count TP, FP, FN
    for yt, yp in zip(y_true, y_pred):
        support[yt] += 1
        if yt == yp:
            tp[yt] += 1
        else:
            fp[yp] += 1
            fn[yt] += 1

    # Accuracy
    accuracy = sum(tp.values()) / n

    # Per-class precision, recall, f1
    precision_c = {}
    recall_c = {}
    f1_c = {}

    for c in classes:
        p = tp[c] / (tp[c] + fp[c]) if (tp[c] + fp[c]) > 0 else 0
        r = tp[c] / (tp[c] + fn[c]) if (tp[c] + fn[c]) > 0 else 0
        f1 = (2 * p * r) / (p + r) if (p + r) > 0 else 0

        precision_c[c] = p
        recall_c[c] = r
        f1_c[c] = f1

    # ---- Averaging ----
    if average == "micro":
        total_tp = sum(tp.values())
        total_fp = sum(fp.values())
        total_fn = sum(fn.values())

        precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
        recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0
        f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    elif average == "macro":
        precision = sum(precision_c.values()) / len(classes)
        recall = sum(recall_c.values()) / len(classes)
        f1 = sum(f1_c.values()) / len(classes)

    elif average == "weighted":
        total = sum(support.values())
        precision = sum(precision_c[c] * support[c] for c in classes) / total
        recall = sum(recall_c[c] * support[c] for c in classes) / total
        f1 = sum(f1_c[c] * support[c] for c in classes) / total

    elif average == "binary":
        c = pos_label
        precision = precision_c[c]
        recall = recall_c[c]
        f1 = f1_c[c]

    else:
        raise ValueError("Invalid averaging method")

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }