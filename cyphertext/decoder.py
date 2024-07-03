"""
This module contain functions to decode text using some common ciphers, along with some custom ciphers.
"""
from typing import List
def caesar(message:str, key:int):
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

def affine(message:str, a:int, b:int):
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

def morse(message:str)-> str:
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

def xor(message : List, key : str) -> str:
    """
    Decodes the given message using the specified key.

    Args:
        message (LIst): The message to be decoded in form of a list of hex values.
        key (str): The key to XOR the message with. can be of any length.

    Returns:
        str: The decoded message.

    """
    message = [int(i,16) for i in message]
    message = ''.join([chr(i) for i in message])
    key = key*((len(message)//len(key)) + 1)  # repeat the key to match the length of the message
    key = key[:len(message)] # trim the key to match the length of the message
    str_result = ""
    for i in range(len(message)):
        str_result += chr(ord(message[i]) ^ ord(key[i]))
    return str_result