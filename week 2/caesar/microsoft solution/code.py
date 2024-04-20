
def caesar_encode(message, key):
    """
    Encodes a message using the Caesar cipher.

    Args:
        message (str): The input message to encode.
        key (int): The shift value for the cipher.

    Returns:
        str: The encoded message.
    """
    encoded_message = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char_ord = (ord(char) - base + key) % 26 + base
            new_char = chr(new_char_ord)
            encoded_message += new_char
        else:
            encoded_message += char
    return encoded_message

def caesar_decode(message, key):
    """
    Decodes a message using the Caesar cipher.

    Args:
        message (str): The input message to decode.
        key (int): The shift value for the cipher.

    Returns:
        str: The decoded message.
    """
    decoded_message = ''
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            let_ord = ord(char)
            new_let_ord = (let_ord - key - base) % 26 + base
            decoded_message += chr(new_let_ord)
        else:
            decoded_message += char
    return decoded_message