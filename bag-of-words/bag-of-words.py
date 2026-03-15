import numpy as np

def bag_of_words_vector(tokens, vocab):
    idx = {w:i for i, w in enumerate(vocab)}
    vec = np.zeros(len(vocab), dtype=int)

    for t in tokens:
        if t in idx:
            vec[idx[t]] += 1

    return vec