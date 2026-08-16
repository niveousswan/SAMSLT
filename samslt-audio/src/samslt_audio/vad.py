import numpy as np
def energy_vad(x, frame=320, threshold=0.01):
    regions=[]; start=None
    for i in range(0,len(x),frame):
        f=x[i:i+frame]
        active=bool(len(f) and np.sqrt(np.mean(f**2))>=threshold)
        if active and start is None:start=i
        if not active and start is not None:regions.append((start,i));start=None
    if start is not None:regions.append((start,len(x)))
    return regions
