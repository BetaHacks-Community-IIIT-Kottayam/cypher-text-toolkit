#!/usr/bin/env python

"""Tests for `cyphertext` package."""


import unittest

from cyphertext import encoder


class TestEncoder(unittest.TestCase):
    """Tests for `encoder` package."""

    # caesar
    def test_Caesar_001(self):
        self.assertEqual(encoder.caesar('Hello, World!', 3), 'KHOOR, ZRUOG!')
    def test_Caesar_002(self):
        self.assertEqual(encoder.caesar('Hello, World!', 0), 'HELLO, WORLD!')
    def test_Caesar_003(self):
        self.assertEqual(encoder.caesar('Hello, World!', 26), 'HELLO, WORLD!')
    def test_Caesar_004(self):
        self.assertEqual(encoder.caesar('Hello, World!', 27), 'IFMMP, XPSME!')
    def test_Caesar_005(self):
        self.assertEqual(encoder.caesar('Hello, World!', 128), 'FCJJM, UMPJB!')
    def test_Caesar_006(self):
        self.assertEqual(encoder.caesar('Hello, World!', -3), 'EBIIL, TLOIA!')
    
    # Piglatin
    def test_Piglatin_001(self):
        self.assertEqual(encoder.piglatin('Hello, World!'), 'elloHay, orldWay!')
    def test_Piglatin_002(self):
        self.assertEqual(encoder.piglatin('Python is fun'), 'onPythay isyay unfay')
    def test_Piglatin_003(self):
        self.assertEqual(encoder.piglatin('Coding is awesome'), 'odingCay isyay awesomeyay')
    def test_Piglatin_004(self):
        self.assertEqual(encoder.piglatin('GitHub Copilot'), 'itHubGay opilotCay')
    def test_Piglatin_005(self):
        self.assertEqual(encoder.piglatin('Artificial Intelligence'), 'Artificialyay Intelligenceyay')
    # Affine
    def test_Affine_001(self):
        self.assertEqual(encoder.affine('A quick brown fox, suddenly jumped over a lazy dog !', 3, 7), 'H DPFNL KGXVU WXY, JPQQTUOB IPRATQ XSTG H OHEB QXZ !')
    def test_Affine_002(self):
        self.assertEqual(encoder.affine('A quick brown fox, suddenly jumped over a lazy dog !', 1, 0), 'A QUICK BROWN FOX, SUDDENLY JUMPED OVER A LAZY DOG !')
    def test_Affine_003(self):
        self.assertEqual(encoder.affine('A quick brown fox, suddenly jumped over a lazy dog !', 5, 12), 'M OIAWK RTESZ LEX, YIBBGZPC FIUJGB ENGT M PMHC BEQ !')
    def test_Affine_004(self):
        self.assertEqual(encoder.affine('A quick brown fox, suddenly jumped over a lazy dog !', 9, 21), 'V JTPNH ESRLI ORU, BTWWFIQD YTZAFW RCFS V QVMD WRX !')
    def test_Affine_005(self):
        self.assertEqual(encoder.affine('A quick brown fox, suddenly jumped over a lazy dog !', 25, 3), 'D NJVBT CMPHQ YPG, LJAAZQSF UJROZA PIZM D SDEF APX !')
    # Morse
    def test_Morse_001(self):
        self.assertEqual(encoder.morse('Hello, World!'), '.... . .-.. .-.. --- , / .-- --- .-. .-.. -.. !')
    def test_Morse_002(self):
        self.assertEqual(encoder.morse('Python is fun'), '.--. -.-- - .... --- -. / .. ... / ..-. ..- -.')
    def test_Morse_003(self):
        self.assertEqual(encoder.morse('12345'), '.---- ..--- ...-- ....- .....')
    def test_Morse_004(self):
        self.assertEqual(encoder.morse('Arificial intelligence'), '.- .-. .. ..-. .. -.-. .. .- .-.. / .. -. - . .-.. .-.. .. --. . -. -.-. .')
    # XOR
    def test_XOR_001(self):
        self.assertEqual(encoder.xor('Hello, World!', 'key'), '23 00 15 07 0a 55 4b 32 16 19 09 1d 4a')
    def test_XOR_002(self):
        self.assertEqual(encoder.xor('Python is fun', 'secret'), '23 1c 17 1a 0a 1a 53 0c 10 52 03 01 1d')
    def test_XOR_003(self):
        self.assertEqual(encoder.xor('Coding is awesome', 'password'), '33 0e 17 1a 19 08 52 0d 03 41 12 04 12 1c 1d 09 15')
    def test_XOR_004(self):
        self.assertEqual(encoder.xor('GitHub Copilot', 'key'), '2c 0c 0d 23 10 1b 4b 26 16 1b 0c 15 04 11')
    def test_XOR_005(self):
        self.assertEqual(encoder.xor('Artificial Intelligence', 'secret'), '32 17 17 1b 03 1d 10 0c 02 1e 45 3d 1d 11 06 1e 09 1d 14 00 0d 11 00')
    # Base64
    def test_Base64_001(self):
        self.assertEqual(encoder.base64('Hello, World!'), 'SGVsbG8sIFdvcmxkIQ==')
    def test_Base64_002(self):
        self.assertEqual(encoder.base64('Python is fun'), 'UHl0aG9uIGlzIGZ1bg==')
    def test_Base64_003(self):
        self.assertEqual(encoder.base64('Coding is awesome'), 'Q29kaW5nIGlzIGF3ZXNvbWU=')
    def test_Base64_004(self):
        self.assertEqual(encoder.base64('GitHub Copilot'), 'R0lGODogQ29waWxvdA==')
    def test_Base64_005(self):
        self.assertEqual(encoder.base64('Artificial Intelligence'), 'QXJ0aWZpY2lhbCBJbnRlbGxpZ2VuY2U=')