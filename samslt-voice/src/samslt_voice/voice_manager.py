class VoiceManager:
    def __init__(self,registry):self.registry=registry
    def voice_for(self,speaker_id):return self.registry.get_or_assign(speaker_id)
