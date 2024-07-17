"""
This module contains functions to encode text using some common ciphers, along with some custom ciphers.
"""
import string
import pybase64
from Crypto.Util.number import inverse, GCD ,long_to_bytes
from sympy import randprime

def caesar(message:str, key:int)-> str:
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

def __remove_punc__(word):
    """
    Removes punctuation from the given word.

    Args:
        word (str): The word to remove punctuation from.

    Returns:
        str: The word without punctuation.

    """
    return_word = ""
    start_punc = ""
    end_punc = ""
    while word[0] not in string.ascii_letters:
        start_punc += word[0]
        word = word[1:]
    while word[-1] not in string.ascii_letters:
        end_punc = word[-1] + end_punc
        word = word[:-1]
    return_word = word
    return return_word, start_punc , end_punc

def piglatin(message:str)-> str:
    """
    Applies the Pig Latin cipher to the given message.

    Args:
        message (str): The message to be encoded.

    Returns:
        str: The encoded message.

    """
    vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    str_result = ""

    for word in message.split():
        word,start_punc,end_punc = __remove_punc__(word)
        if word[0] in vowels:
            str_result += start_punc + word + "yay" + end_punc + " "
        elif word.isalpha():
            while word[0] not in vowels:
                word = word[1:] + word[0]
            str_result += start_punc + word + "ay" + end_punc + " "
        else:
            str_result += start_punc + end_punc + " "
    return str_result.strip()

def affine(message:str, a:int, b:int)-> str:
    """
    Applies the Affine cipher to the given message using the specified keys.

    Args:
        message (str): The message to be encoded.
        a (int): The first key.
        b (int): The second key.

    Returns:
        str: The encoded message.

    """
    str_result = ""
    message = message.upper()
    for char in message:
        if char.isalpha() == False:
            str_result += char
            continue
        n = ord(char)
        n -= 65
        n = ((n * a) + b) % 26
        n += 65
        str_result += chr(n)

    return str_result

def morse(message:str) -> str:
    """
    Applies the Morse code cipher to the given message.

    Args:
        message (str): The message to be encoded.

    Returns:
        str: The encoded message.

    """
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', '0': '-----',
        ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
    }
    str_result = ""
    for char in message:
        if char.isalpha():
            str_result += morse_code[char.upper()] + " "
        elif char.isdigit():
            str_result += morse_code[char] + " "
        elif char == " ":
            str_result += "/ "
        else:
            str_result += char + " "
    return str_result.strip()

def xor(message : str, key : str) -> str:
    """
    Applies the XOR cipher to the given message using the specified key.

    Args:
        message (str): The message to be encoded.
        key (str): The key to XOR the message with. can be of any length.

    Returns:
        str: The encoded message.

    """
    key = key*((len(message)//len(key)) + 1)  # repeat the key to match the length of the message
    key = key[:len(message)] # trim the key to match the length of the message
    str_result = ""
    for i in range(len(message)):
        str_result += chr(ord(message[i]) ^ ord(key[i]))
    return ' '.join(format(ord(c), '02x') for c in str_result)

def base64(message:str)-> str:
    """
    Encode the given string using Base64 encoding.

    Parameters:
    message (str): The string to be encoded.

    Returns:
    str: The Base64 encoded string.
    """
    # Convert the input string to bytes
    byte_string = message.encode('utf-8')
    
    # Encode the byte string using Base64
    base64_bytes = pybase64.b64encode(byte_string)
    
    # Convert the Base64 bytes back to a string
    base64_string = base64_bytes.decode('utf-8')
    
    return base64_string

def generate_rsa_keys(p:int, q:int)->tuple:
    """
    Generate RSA modulus, private key, and public key from two prime numbers.

    Parameters:
    p (int): A prime number.
    q (int): Another prime number.

    Returns:
    tuple: A tuple containing the modulus (n), private key (d), and public key (e).
    """
    # Calculate n
    n = p * q
    
    # Calculate the totient
    phi_n = (p - 1) * (q - 1)
    
    # Choose public exponent e (commonly 65537)
    e = 65537
    if GCD(e, phi_n) != 1:
        raise ValueError("e and phi(n) are not coprime. Choose a different e.")
    
    # Calculate the private exponent d
    d = inverse(e, phi_n)
    
    return n, e, d

def get_random_keys(bits=1024)-> tuple:
    """
    Generate random prime numbers p and q of the specified bit length (default 1024).
    Then generate RSA modulus, private key, and public key from these prime numbers.

    Parameters:
    bits (int): The bit length of the prime numbers. Default is 1024.

    Returns:
    tuple: A tuple containing the modulus (n), private key (d), and public key (e).
    """
    # Generate random prime p
    p = randprime(2**(bits//2), 2**(bits//2 + 1))
    
    # Generate random prime q, ensuring it's different from p
    while True:
        q = randprime(2**(bits//2), 2**(bits//2 + 1))
        if q != p:
            break
    
    return generate_rsa_keys(p, q)

def rsa(n:int, c:str, d:int ,string_output=False)-> str:
    """
    Decrypt an RSA encrypted message.

    Parameters:
    n (int): The modulus (product of two prime numbers p and q).
    c (str): The message .
    d (int): The exponent key.
    string_output (bool): If True, the decrypted message will be returned as a string if possible. Otherwise, it will be returned as an integer.

    Returns:
    str: The decrypted message.
    """
    try:
        c=int(c)
    except:
        pass
    if not isinstance(c,int):
        c=c.encode('utf-8')
        c=int.from_bytes(c, 'big')
    # Decrypt the message using RSA formula: m = c^d % n
    m = pow(c, d, n)
    if string_output:
        try:
            return long_to_bytes(m).decode('utf-8')
        except:
            return str(m)
    return str(m)
