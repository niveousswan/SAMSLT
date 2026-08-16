from dataclasses import dataclass

@dataclass(frozen=True)
class SpeakerSegment:
    start: float
    end: float
    speaker_id: str

@dataclass(frozen=True)
class OverlapRegion:
    start: float
    end: float
    speaker_ids: tuple[str, ...]

@dataclass
class TranslationEvent:
    start: float
    end: float
    speaker_id: str
    source_text: str
    target_text: str
    voice_id: str
