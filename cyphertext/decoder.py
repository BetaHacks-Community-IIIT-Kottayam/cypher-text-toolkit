"""
This module contain functions to decode text using some common ciphers, along with some custom ciphers.
"""
def caesar(message, key):
    """
    Decode a message encrypted using the Caesar cipher.

    Args:
        message (str): The encrypted message to be decoded.
        key (int): The key used for encryption.

    Returns:
        str: The decoded message.

    """
    message = message.upper()
    str_result = ""

    for char in message:
        if char.isalpha():
            n = ord(char)
            n -= 65
            n = ((n - key) % 26)
            n += 65
            str_result += chr(n)
        else:
            str_result += char
    return str_result

def affine(message, a, b):
    """
    Decode a message encrypted using the Affine cipher.

    Args:
        message (str): The encrypted message to be decoded.
        a (int): The first key used for encryption.
        b (int): The second key used for encryption.

    Returns:
        str: The decoded message.

    """
    message = message.upper()
    str_result = ""
    for char in message:
        if char.isalpha() == False:
            str_result += char
            continue
        n = ord(char)
        n -= 65  
        key_inverse = pow(a, -1, 26)
        n = ((n-b) * key_inverse) % 26
        n += 65 
        str_result += chr(n)
        
    return str_result

def morse(message):
    """
    Decode a message encrypted using the Morse cipher.

    Args:
        message (str): The encrypted message to be decoded.

    Returns:
        str: The decoded message.

    """
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
        '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
    }
    inv_morse_code = {v: k for k, v in morse_code.items()}
    str_result = ""
    message = message.split(" ")
    for char in message:
        if char in inv_morse_code:
            str_result += inv_morse_code[char]
        else:
            str_result += char
    return str_result