"""
This module contains functions to encode text using some common ciphers, along with some custom ciphers.
"""

def ascii_shift(plaintext, shift):
    """
    Shifts each character in the plaintext by the given shift value and returns the resulting ciphertext.

    Args:
        plaintext (str): The input string to be encoded.
        shift (int): The amount by which each character should be shifted.

    Returns:
        str: The encoded ciphertext.

    Example:
        >>> ascii_shift("Hello, World!", 3)
        'Khoor/#Zruog!'
    """
    ciphertext = ""
    for char in plaintext:
        shifted_char = chr((ord(char) + shift) % 128)  # Assuming ASCII characters (0-127)
        ciphertext += shifted_char
    return ciphertext