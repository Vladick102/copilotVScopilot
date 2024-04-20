"""
Function of caesar code
"""


def caesar_encode(message, key):
    """
    Returns ceasar_encode
    >>> caesar_encode('computer', 3)
    'frpsxwhu'
    """
    encoded_message = ""
    for i in message:
        if i == " ":
            encoded_message += i
        else:
            let_ord = ord(i)
            new_let_ord = let_ord + key
            if new_let_ord > 122:
                while new_let_ord > 122:
                    new_let_ord -= 26
            new_let = chr(new_let_ord)
            encoded_message += new_let
    return encoded_message


def caesar_decode(message, key):
    """
    Returns caesar_decode
    >>> caesar_decode('xa xcd s', 5)
    'sv sxy n'
    """
    decoded_message = ""
    for i in message:
        if i == " ":
            decoded_message += i
        else:
            let_ord = ord(i)
            new_let_ord = let_ord - key
            if new_let_ord < 97:
                while new_let_ord < 97:
                    new_let_ord += 26
            new_let = chr(new_let_ord)
            decoded_message += new_let
    return decoded_message
