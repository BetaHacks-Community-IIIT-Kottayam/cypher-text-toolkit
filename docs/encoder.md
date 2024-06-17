
# Encoder module

The encoder module provides functions for encoding and decoding data using a variety of encoding schemes.

## Functions
1. Caesar cipher
2. Pig Latin

## Caesar cipher
The Caesar cipher is a substitution cipher that shifts the alphabet by a fixed number of positions. For example, with a shift of 1, A would be replaced by B, B would become C, and so on.
### Arguments
- `message` (str): The text to be encoded.
- `key` (int): The number of positions to shift the alphabet.
### Returns
- `str`: The encoded message.
### Usage
```python
from cyphertext import encoder
cipher = encoder.caesar('hello', 1)
print(cipher)
```
### Output
```
ifmmp
```

## Pig Latin
Pig Latin is a language game where words are altered according to a simple set of rules. To form a word in Pig Latin, move the initial consonant or consonant cluster to the end of the word and add "ay". If the word begins with a vowel, simply add "yay" to the end.

### Arguments
- `message` (str): The word to be encoded.
### Returns
- `str`: The encoded word.

### Usage
```python
from cyphertext import encoder
cipher = encoder.pig_latin('hello')
print(cipher)
```
### Output
```
'ellohay'
```
