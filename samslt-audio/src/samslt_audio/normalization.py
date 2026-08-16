import numpy as np
def peak_normalize(x, peak=.98):
    m=float(np.max(np.abs(x))) if len(x) else 0.0
    return x if m==0 else x*(peak/m)
