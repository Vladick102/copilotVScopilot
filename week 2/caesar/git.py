def caesar_encode(message, key):
    """
    Returns ceasar_encode
    >>> caesar_encode('computer', 3)
    'frpsxwhu'
    """
    encoded_message = ""
    for char in message:
        if char.isalpha():
            offset = ord("a") if char.islower() else ord("A")
            encoded_message += chr((ord(char) - offset + key) % 26 + offset)
        else:
            encoded_message += char
    return encoded_message


def caesar_decode(message, key):
    """
    Returns caesar_decode
    >>> caesar_decode('xa xcd s', 5)
    'sv sxy n'
    """
    return caesar_encode(message, -key)
