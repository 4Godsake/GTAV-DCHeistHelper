from image import w, h
from keyboard_input import keys


class Fingerprint:
    def __init__(self, x1, y1, x2, y2, key_code):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.key_code = key_code


FINGERPRINTS = (Fingerprint(w * 0.248, h * 0.252, w * 0.308, h * 0.358, keys.get('down')),
                Fingerprint(w * 0.248, h * 0.384, w * 0.308, h * 0.492, keys.get('down')),
                Fingerprint(w * 0.248, h * 0.519, w * 0.308, h * 0.625, keys.get('down')),
                Fingerprint(w * 0.248, h * 0.652, w * 0.308, h * 0.758, keys.get('right')),
                Fingerprint(w * 0.323, h * 0.652, w * 0.383, h * 0.758, keys.get('up')),
                Fingerprint(w * 0.323, h * 0.519, w * 0.383, h * 0.625, keys.get('up')),
                Fingerprint(w * 0.323, h * 0.384, w * 0.383, h * 0.492, keys.get('up')),
                Fingerprint(w * 0.323, h * 0.252, w * 0.383, h * 0.358, keys.get('left')))
