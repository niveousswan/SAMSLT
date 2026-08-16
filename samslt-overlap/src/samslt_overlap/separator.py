class SpeechSeparator:
    def __init__(self, backend=None): self.backend=backend
    def separate(self, waveform, sample_rate):
        if self.backend is None: raise RuntimeError("Configure a separation backend")
        return self.backend(waveform, sample_rate)
