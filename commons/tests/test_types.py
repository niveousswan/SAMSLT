from samslt_commons.types import SpeakerSegment

def test_segment():
    s=SpeakerSegment(0,1,"A")
    assert s.end-s.start==1
