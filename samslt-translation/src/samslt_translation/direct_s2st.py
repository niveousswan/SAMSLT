class DirectS2ST:
    def __init__(self,backend=None):self.backend=backend
    def translate(self,x,sr,source,target):
        if self.backend is None:raise RuntimeError("Configure direct S2ST backend")
        return self.backend(x,sr,source,target)
