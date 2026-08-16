def sort_segments(segments):
    return sorted(segments,key=lambda s:(s.start,s.end,s.speaker_id))
