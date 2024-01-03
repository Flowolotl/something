from enum import Enum


class Voice(Enum):
    Chad = 1
    Nvim = 2
    Yippee = 3
    Cheese = 4


Voices = [voice.name for voice in Voice]