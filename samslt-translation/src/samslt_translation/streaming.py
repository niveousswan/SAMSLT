class StreamingSpeechTranslator:
    def __init__(self,asr,mt): self.asr,self.mt=asr,mt
    def translate_chunk(self,x,sr,source,target):
        source_text=self.asr.transcribe(x,sr)
        target_text=self.mt.translate(source_text,source,target)
        return {"source_text":source_text,"target_text":target_text}
