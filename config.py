from voice import Voice, Voices
from character import Character


class _config:

    def __init__(self, num_char=1, default=Voice.Chad):
        self.default = default
        self.num_characters = num_char
        self.voice_selection = default
        self.characters: [Character] = []
        for x in range(self.num_characters):
            self._add(voice=default)


    def _add(self, voice=None) -> Character:
        self.num_characters += 1
        newChar = Character(voice=voice or self.default)
        self.characters.append(newChar)
        return newChar


    def add(self, voice=None) -> Character:
        self.num_characters += 1
        return self._add(voice)
    

    def __str__(self) -> str:
        return f"Config({self.voice})"

