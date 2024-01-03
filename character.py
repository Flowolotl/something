from voice import Voice, Voices


class Character:

    def __init__(self, voice=Voice.Chad):
        self.voice: Voice = voice


    def voice_name(self) -> str:
        return self.voice.name


    def __str__(self) -> str:
        return f"Character({self.voice})"
    
