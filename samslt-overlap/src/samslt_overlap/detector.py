from samslt_commons.types import OverlapRegion

def detect_overlaps(segments):
    bounds=sorted({t for s in segments for t in (s.start,s.end)})
    out=[]
    for a,b in zip(bounds,bounds[1:]):
        active=tuple(sorted({s.speaker_id for s in segments if s.start<b and s.end>a}))
        if len(active)>=2:
            out.append(OverlapRegion(a,b,active))
    return out
