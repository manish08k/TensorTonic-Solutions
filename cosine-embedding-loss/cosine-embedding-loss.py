import numpy as np

def cosine_embedding_loss(x1, x2, label, margin):
    x1 = np.asarray(x1, dtype=float)
    x2 = np.asarray(x2, dtype=float)

    # Cosine similarity
    dot = np.dot(x1, x2)
    norm1 = np.linalg.norm(x1)
    norm2 = np.linalg.norm(x2)
    cos_sim = dot / (norm1 * norm2)

    # Loss calculation
    if label == 1:
        return float(1 - cos_sim)
    else:  # label == -1
        return float(max(0.0, cos_sim - margin))