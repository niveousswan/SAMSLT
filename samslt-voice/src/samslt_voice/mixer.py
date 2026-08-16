import numpy as np
def mix_tracks(tracks):
    if not tracks:return np.zeros(0,dtype=np.float32)
    n=max(len(x) for x in tracks)
    out=np.zeros(n,dtype=np.float32)
    for x in tracks: out[:len(x)]+=x
    peak=float(np.max(np.abs(out))) if out.size else 0
    return out if peak<=1 else out/peak
