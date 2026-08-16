CREATE TABLE IF NOT EXISTS sessions (
  session_id TEXT PRIMARY KEY,
  source_language TEXT,
  target_language TEXT,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS speakers (
  session_id TEXT NOT NULL,
  speaker_id TEXT NOT NULL,
  embedding BLOB,
  first_seen REAL,
  last_seen REAL,
  PRIMARY KEY(session_id, speaker_id)
);

CREATE TABLE IF NOT EXISTS voice_assignments (
  session_id TEXT NOT NULL,
  speaker_id TEXT NOT NULL,
  target_voice_id TEXT NOT NULL,
  assigned_at TEXT DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY(session_id, speaker_id)
);

CREATE TABLE IF NOT EXISTS translation_events (
  event_id INTEGER PRIMARY KEY AUTOINCREMENT,
  session_id TEXT NOT NULL,
  speaker_id TEXT NOT NULL,
  start REAL,
  end REAL,
  source_text TEXT,
  target_text TEXT,
  target_voice_id TEXT,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
