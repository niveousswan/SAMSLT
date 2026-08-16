def validate_segments(segments):
    return all(s.end>=s.start and bool(s.speaker_id) for s in segments)
