def word_count_dict(sentences):
    freq = {}
    for sent in sentences:
        for word in sent:
            freq[word] = freq.get(word, 0) + 1
    return freq