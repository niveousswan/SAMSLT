class ASR:
    def __init__(self,backend=None):self.backend=backend
    def transcribe(self,x,sr):
        if self.backend is None:raise RuntimeError("Configure ASR backend")
        return self.backend(x,sr)
