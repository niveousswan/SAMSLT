class NeuralVocoder:
    def __init__(self,backend=None):self.backend=backend
    def generate(self,features):
        if self.backend is None:raise RuntimeError("Configure neural vocoder")
        return self.backend(features)
