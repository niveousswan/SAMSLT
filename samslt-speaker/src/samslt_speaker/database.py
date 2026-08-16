import sqlite3
from pathlib import Path

SCHEMA = '''CREATE TABLE IF NOT EXISTS sessions(session_id TEXT PRIMARY KEY,source_language TEXT,target_language TEXT,created_at TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS speakers(session_id TEXT,speaker_id TEXT,embedding BLOB,first_seen REAL,last_seen REAL,PRIMARY KEY(session_id,speaker_id));
CREATE TABLE IF NOT EXISTS voice_assignments(session_id TEXT,speaker_id TEXT,target_voice_id TEXT,assigned_at TEXT DEFAULT CURRENT_TIMESTAMP,PRIMARY KEY(session_id,speaker_id));'''

class SpeakerDatabase:
    def __init__(self,path):
        Path(path).parent.mkdir(parents=True,exist_ok=True)
        self.conn=sqlite3.connect(path)
        self.conn.executescript(SCHEMA)
        self.conn.commit()
    def close(self): self.conn.close()
