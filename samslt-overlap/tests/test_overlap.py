from samslt_commons.types import SpeakerSegment
from samslt_overlap.detector import detect_overlaps
def test_overlap():
    o=detect_overlaps([SpeakerSegment(0,2,"A"),SpeakerSegment(1,3,"B")])
    assert o[0].start==1 and o[0].end==2
