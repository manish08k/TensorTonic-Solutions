def text_chunking(tokens, chunk_size, overlap):
    result = []
    n = len(tokens)

    step = chunk_size - overlap

    for i in range(0, n, step):
        chunk = tokens[i:i + chunk_size]
        result.append(chunk)

        # Stop if we reached the end
        if i + chunk_size >= n:
            break

    return result