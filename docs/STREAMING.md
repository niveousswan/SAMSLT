# Streaming

The repository separates streaming policy from model backends.

A validated real-time implementation should define:
- input chunk size;
- buffering;
- incremental diarization state;
- partial ASR hypothesis handling;
- translation policy;
- synthesis buffering;
- output scheduling;
- stage and end-to-end latency.
