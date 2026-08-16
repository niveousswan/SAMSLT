from samslt_commons.types import SpeakerSegment
from samslt_diarization.validation import validate_segments
def test_validation(): assert validate_segments([SpeakerSegment(0,1,"A")])
