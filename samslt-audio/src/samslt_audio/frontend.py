from .noise_suppression import suppress_noise
from .normalization import peak_normalize

class AudioFrontEnd:
    def process(self, waveform):
        return peak_normalize(suppress_noise(waveform))
