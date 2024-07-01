"""
This module contains functions to encode text using some common ciphers, along with some custom ciphers.
"""
import string
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

def piglatin(message):
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

def affine(message, a, b):
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