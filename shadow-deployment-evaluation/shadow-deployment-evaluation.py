import math

def evaluate_shadow(production_log, shadow_log, criteria):
    """
    Evaluate whether a shadow model is ready for promotion.
    """

    n = len(production_log)

    # Production accuracy
    production_correct = sum(
        1 for row in production_log
        if row["prediction"] == row["actual"]
    )
    production_accuracy = production_correct / n

    # Shadow accuracy
    shadow_correct = sum(
        1 for row in shadow_log
        if row["prediction"] == row["actual"]
    )
    shadow_accuracy = shadow_correct / n

    # Accuracy gain
    accuracy_gain = shadow_accuracy - production_accuracy

    # P95 latency (nearest-rank method)
    latencies = sorted(row["latency_ms"] for row in shadow_log)
    index = math.ceil(0.95 * n) - 1
    shadow_latency_p95 = latencies[index]

    # Agreement rate
    agreements = sum(
        1 for p, s in zip(production_log, shadow_log)
        if p["prediction"] == s["prediction"]
    )
    agreement_rate = agreements / n

    # Promotion decision
    promote = (
        accuracy_gain >= criteria["min_accuracy_gain"]
        and shadow_latency_p95 <= criteria["max_latency_p95"]
        and agreement_rate >= criteria["min_agreement_rate"]
    )

    return {
        "promote": promote,
        "metrics": {
            "shadow_accuracy": shadow_accuracy,
            "production_accuracy": production_accuracy,
            "accuracy_gain": accuracy_gain,
            "shadow_latency_p95": shadow_latency_p95,
            "agreement_rate": agreement_rate
        }
    }