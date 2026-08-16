import numpy as np
def cosine_similarity(a,b):
    return float(np.dot(a,b)/((np.linalg.norm(a)+1e-12)*(np.linalg.norm(b)+1e-12)))
