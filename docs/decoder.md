# Decoder module

The decoder module provides functions for decoding data using a variety of decoding schemes.

## Functions
1. Caesar cipher

## Caesar cipher
The Caesar cipher is a substitution cipher that shifts the alphabet by a fixed number of positions. For example, with a shift of 1, A would be replaced by B, B would become C, and so on.

### Arguments
- `message` (str): The text to be decoded.
- `key` (int): The number of positions to shift the alphabet.

### Returns
- `str`: The decoded message.

### Usage
```python
from cyphertext import decoder
decoded = decoder.caesar('ifmmp', 1)
print(decoded)
```
### Output
```
'hello'
```
