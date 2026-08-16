from samslt_speaker.database import SpeakerDatabase
from samslt_speaker.psvr import PersistentSpeakerVoiceRegistry
def test_psvr(tmp_path):
    db=SpeakerDatabase(str(tmp_path/"x.sqlite"))
    r=PersistentSpeakerVoiceRegistry(db,"s",["v1","v2"])
    assert r.get_or_assign("A")==r.get_or_assign("A")=="v1"
    db.close()
