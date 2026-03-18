def f1_micro(y_true, y_pred) -> float:
    tp = sum(t == p for t, p in zip(y_true, y_pred))
    n = len(y_true)
    return tp / n if n else 0.0