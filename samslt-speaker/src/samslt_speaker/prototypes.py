import numpy as np
def mean_prototype(embeddings):
    p=np.mean(np.stack(embeddings),axis=0)
    return p/(np.linalg.norm(p)+1e-12)
