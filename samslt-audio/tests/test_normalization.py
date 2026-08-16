import numpy as np
from samslt_audio.normalization import peak_normalize
def test_peak():
    x=peak_normalize(np.array([0.,2.],dtype=np.float32))
    assert round(float(x.max()),2)==0.98
