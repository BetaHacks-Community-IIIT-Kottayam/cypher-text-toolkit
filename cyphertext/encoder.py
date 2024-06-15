"""
This module contains functions to encode text using some common ciphers, along with some custom ciphers.
"""

def caesar(message, key):
    """
    Applies the Caesar cipher to the given message using the specified key.

    Args:
        message (str): The message to be encoded.
        key (int): The key to shift the characters by.

    Returns:
        str: The encoded message.

    """
    message = message.upper()
    str_result = ""

    for char in message:
        if char.isalpha():
            n = ord(char)
            n -= 65
            n = ((n + key) % 26)
            n += 65
            str_result += chr(n)
        else:
            str_result += char
    return str_result

def piglatin(message):
    """
    Applies the Pig Latin cipher to the given message.

    Args:
        message (str): The message to be encoded.

    Returns:
        str: The encoded message.

    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    message = message.lower()
    str_result = ""

    for word in message.split():
        if word[0] in vowels:
            str_result += word + "yay "
        else:
            while word[0] not in vowels:
                word = word[1:] + word[0]
            str_result += word + "ay "
    return str_result

