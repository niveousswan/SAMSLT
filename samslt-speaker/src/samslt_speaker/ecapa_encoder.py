import numpy as np
class ECAPAEncoder:
    def __init__(self,backend=None):self.backend=backend
    def encode(self,x,sr):
        if self.backend is None:raise RuntimeError("Configure ECAPA-TDNN backend")
        e=np.asarray(self.backend(x,sr),dtype=np.float32)
        return e/(np.linalg.norm(e)+1e-12)
