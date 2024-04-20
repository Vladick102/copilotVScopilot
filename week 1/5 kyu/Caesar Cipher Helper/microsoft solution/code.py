class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def encode(self, st):
        result = ""
        for char in st:
            if char.isalpha():
                # Shift the character by the specified amount
                shifted_char = chr(((ord(char.upper()) - ord('A') + self.shift) % 26) + ord('A'))
                result += shifted_char
            else:
                # Leave non-alphabetic characters unchanged
                result += char
        return result

    def decode(self, st):
        result = ""
        for char in st:
            if char.isalpha():
                # Shift the character back by the specified amount
                shifted_char = chr(((ord(char.upper()) - ord('A') - self.shift) % 26) + ord('A'))
                result += shifted_char
            else:
                # Leave non-alphabetic characters unchanged
                result += char
        return result