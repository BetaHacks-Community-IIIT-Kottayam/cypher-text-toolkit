"""
This module contain functions to decode text using some common ciphers, along with some custom ciphers.
"""
import base64

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


# this function is not working for frequencies below 500Hz
# def morse_audio(file_path:str)->str:
#     """
#     Decodes Morse code from an audio file.

#     Args:
#         file_path (str): The path to the audio file.

#     Returns:
#         str: The decoded Morse code.

#     """
#     warnings.filterwarnings("ignore", category=FutureWarning)
#     sample_rate, data = wavfile.read(file_path)
#     if data.ndim > 1:
#         data = np.mean(data, axis=1)
#     time = np.linspace(0, len(data) / sample_rate, len(data))
#     df = pd.DataFrame({'Time': time, 'Amplitude': data})
#     df['Amplitude'] = np.where(df['Amplitude'] == 128, 0, 128)
#     changes = np.diff(df['Amplitude']) != 0
#     segment_indices = np.flatnonzero(changes) + 1
#     segments = np.split(df, segment_indices)
#     heights = sorted(set(len(seg) for seg in segments if seg['Amplitude'].iloc[0] == 128), reverse=True)
#     spaces = sorted(set(len(seg) for seg in segments if seg['Amplitude'].iloc[0] == 0), reverse=True)
#     decode_dict = {
#         heights[0]: '-',
#         heights[1]: '.',
#         spaces[0]: ' / ',
#         spaces[1]: ' ',
#     }
#     width_arr = [len(seg) for seg in segments if len(seg) > 10]
#     decoded_morse_code = ''.join(decode_dict.get(width, '') for width in width_arr)
#     return morse(decoded_morse_code)

def base64(message:str)-> str:
    """
    Decode the given Base64 encoded string.

    Parameters:
    message (str): The Base64 encoded string to be decoded.

    Returns:
    str: The decoded string.
    """
    # Convert the Base64 encoded string to bytes
    base64_bytes = message.encode('utf-8')
    
    # Decode the Base64 bytes
    byte_string = base64.b64decode(base64_bytes)
    
    # Convert the decoded bytes back to a string
    decoded_string = byte_string.decode('utf-8')
    
    return decoded_string