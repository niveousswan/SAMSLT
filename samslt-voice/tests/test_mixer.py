import numpy as np
from samslt_voice.mixer import mix_tracks
def test_mix():
    x=mix_tracks([np.array([.2,.2]),np.array([.2,.2])])
    assert len(x)==2
