"""
This module contains functions to encode text using some common ciphers, along with some custom ciphers.
"""

def ceaser(message, key):
    """
    Applies the Ceaser cipher to the given message using the specified key.

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

print(f"self.assertEqual(ascii_shift('Hello, World!', 3), '{ceaser("Hello, World!", 3)}')")
print(f"self.assertEqual(ascii_shift('Hello, World!', 0), '{ceaser("Hello, World!", 0)}')")
print(f"self.assertEqual(ascii_shift('Hello, World!', 26), '{ceaser("Hello, World!", 26)}')")
print(f"self.assertEqual(ascii_shift('Hello, World!', 27), '{ceaser("Hello, World!", 27)}')")
print(f"self.assertEqual(ascii_shift('Hello, World!', 128), '{ceaser("Hello, World!", 128)}')")
print(f"self.assertEqual(ascii_shift('Hello, World!', -3), '{ceaser("Hello, World!", -3)}')")