def detect_drift(reference_counts, production_counts, threshold):
    ref_total = sum(reference_counts)
    prod_total = sum(production_counts)
    
    ref_probs = [x / ref_total for x in reference_counts]
    prod_probs = [x / prod_total for x in production_counts]
    
    # Step 2: Compute TVD
    tvd = 0.5 * sum(abs(p - q) for p, q in zip(ref_probs, prod_probs))
    
    # Step 3: Check drift
    drift_detected = tvd > threshold
    
    return {
        "score": tvd,
        "drift_detected": drift_detected
    }