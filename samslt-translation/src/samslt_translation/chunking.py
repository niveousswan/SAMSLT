def iter_chunks(x,chunk_samples):
    for i in range(0,len(x),chunk_samples):
        yield x[i:i+chunk_samples]
