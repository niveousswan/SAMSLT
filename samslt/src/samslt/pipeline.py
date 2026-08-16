class SAMSLTPipeline:
    def __init__(self,source_language=None,target_language=None,**components):
        self.source_language=source_language
        self.target_language=target_language
        self.components=components
    def describe(self):
        return {
            "source_language":self.source_language,
            "target_language":self.target_language,
            "speaker_identity_pathway":["audio","overlap","diarization","speaker encoder","PSVR"],
            "translation_pathway":["ASR/MT or direct S2ST"],
            "synthesis":["speaker-conditioned synthesis","neural vocoder"]
        }
