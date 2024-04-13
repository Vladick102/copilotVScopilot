class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encode(self, text):
        return "".join(
            chr((ord(c) - 65 + self.shift) % 26 + 65) if c.isalpha() else c
            for c in text.upper()
        )

    def decode(self, text):
        return "".join(
            chr((ord(c) - 65 - self.shift) % 26 + 65) if c.isalpha() else c
            for c in text.upper()
        )
