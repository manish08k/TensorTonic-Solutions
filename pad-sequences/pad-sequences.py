import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    # Handle empty input
    if len(seqs) == 0:
        return np.zeros((0, 0), dtype=int)

    # Determine max_len
    if max_len is None:
        max_len = max(len(seq) for seq in seqs)

    N = len(seqs)
    result = np.full((N, max_len), pad_value, dtype=int)

    for i, seq in enumerate(seqs):
        # Truncate if needed
        trunc = seq[:max_len]

        # Place into result (right padding)
        result[i, :len(trunc)] = trunc

    return result