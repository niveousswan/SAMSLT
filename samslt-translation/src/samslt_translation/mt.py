class MachineTranslator:
    def __init__(self,backend=None):self.backend=backend
    def translate(self,text,source,target):
        if self.backend is None:raise RuntimeError("Configure MT backend")
        return self.backend(text,source,target)
