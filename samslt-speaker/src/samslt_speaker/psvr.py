class PersistentSpeakerVoiceRegistry:
    def __init__(self,db,session_id,voices):
        if not voices: raise ValueError("At least one target voice required")
        self.db,self.session_id,self.voices=db,session_id,voices
    def get_or_assign(self,speaker_id):
        row=self.db.conn.execute(
            "SELECT target_voice_id FROM voice_assignments WHERE session_id=? AND speaker_id=?",
            (self.session_id,speaker_id)
        ).fetchone()
        if row:return row[0]
        n=self.db.conn.execute(
            "SELECT COUNT(*) FROM voice_assignments WHERE session_id=?",(self.session_id,)
        ).fetchone()[0]
        voice=self.voices[n%len(self.voices)]
        self.db.conn.execute(
            "INSERT INTO voice_assignments(session_id,speaker_id,target_voice_id) VALUES(?,?,?)",
            (self.session_id,speaker_id,voice)
        )
        self.db.conn.commit()
        return voice
