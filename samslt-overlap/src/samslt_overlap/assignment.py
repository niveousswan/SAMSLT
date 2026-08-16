def assign_streams(stream_embeddings, speaker_prototypes, similarity_fn):
    result=[]
    for emb in stream_embeddings:
        scores=[(spk,similarity_fn(emb,p)) for spk,p in speaker_prototypes.items()]
        result.append(max(scores,key=lambda x:x[1]) if scores else (None,None))
    return result
