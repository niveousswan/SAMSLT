from samslt_speaker.database import SpeakerDatabase
from samslt_speaker.psvr import PersistentSpeakerVoiceRegistry

db=SpeakerDatabase("demo.sqlite")
registry=PersistentSpeakerVoiceRegistry(db,"session-001",["voice_A","voice_B"])
print(registry.get_or_assign("SPEAKER_00"))
print(registry.get_or_assign("SPEAKER_01"))
print(registry.get_or_assign("SPEAKER_00"))
db.close()
