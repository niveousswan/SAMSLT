class AcousticSynthesizer:
    def __init__(self,backend=None):self.backend=backend
    def synthesize(self,text,voice_id):
        if self.backend is None:raise RuntimeError("Configure acoustic synthesizer")
        return self.backend(text=text,voice_id=voice_id)
