from .similarity import cosine_similarity
def best_match(e,prototypes):
    scores=[(s,cosine_similarity(e,p)) for s,p in prototypes.items()]
    return max(scores,key=lambda x:x[1]) if scores else (None,None)
