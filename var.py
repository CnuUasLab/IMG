from enum import Enum

mode = Enum('mode', 'orig cropped')

class imageType:
    cropped, original, none = range(3)
