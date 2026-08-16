class SpeakerDiarizer:
    def __init__(self, backend=None): self.backend=backend
    def diarize(self, audio_path):
        if self.backend is None: raise RuntimeError("Configure a diarization backend")
        return self.backend(audio_path)
