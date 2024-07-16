#!/usr/bin/env python

import unittest

from cyphertext import decoder

class TestDecoder(unittest.TestCase):
    """Tests for `decoder` package."""
    # caesar
    def test_Caesar_001(self):
        self.assertEqual(decoder.caesar('KHOOR, ZRUOG!', 3), 'HELLO, WORLD!')
    def test_Caesar_002(self):
        self.assertEqual(decoder.caesar('HELLO, WORLD!', 0), 'HELLO, WORLD!')
    def test_Caesar_003(self):
        self.assertEqual(decoder.caesar('HELLO, WORLD!', 26), 'HELLO, WORLD!')
    def test_Caesar_004(self):
        self.assertEqual(decoder.caesar('IFMMP, XPSME!', 27), 'HELLO, WORLD!')
    def test_Caesar_005(self):
        self.assertEqual(decoder.caesar('FCJJM, UMPJB!', 128), 'HELLO, WORLD!')
    def test_Caesar_006(self):
        self.assertEqual(decoder.caesar('EBIIL, TLOIA!', -3), 'HELLO, WORLD!')
    # affine
    def test_Affine_001(self):
        self.assertEqual(decoder.affine('H DPFNL KGXVU WXY, JPQQTUOB IPRATQ XSTG H OHEB QXZ !', 3, 7), 'A QUICK BROWN FOX, SUDDENLY JUMPED OVER A LAZY DOG !')
    def test_Affine_002(self):
        self.assertEqual(decoder.affine('A QUICK BROWN FOX, SUDDENLY JUMPED OVER A LAZY DOG !', 1, 0), 'A QUICK BROWN FOX, SUDDENLY JUMPED OVER A LAZY DOG !')
    def test_Affine_003(self):
        self.assertEqual(decoder.affine('M OIAWK RTESZ LEX, YIBBGZPC FIUJGB ENGT M PMHC BEQ !', 5, 12), 'A QUICK BROWN FOX, SUDDENLY JUMPED OVER A LAZY DOG !')
    def test_Affine_004(self):
        self.assertEqual(decoder.affine('V JTPNH ESRLI ORU, BTWWFIQD YTZAFW RCFS V QVMD WRX !', 9, 21), 'A QUICK BROWN FOX, SUDDENLY JUMPED OVER A LAZY DOG !')
    def test_Affine_005(self):
        self.assertEqual(decoder.affine('D NJVBT CMPHQ YPG, LJAAZQSF UJROZA PIZM D SDEF APX !', 25, 3), 'A QUICK BROWN FOX, SUDDENLY JUMPED OVER A LAZY DOG !')
    # Morse
    def test_Morse_001(self):
        self.assertEqual(decoder.morse(".... . .-.. .-.. --- , / .-- --- .-. .-.. -.. !"),"HELLO, WORLD!")
    def test_Morse_002(self):
        self.assertEqual(decoder.morse(".--. -.-- - .... --- -. / .. ... / ..-. ..- -."),"PYTHON IS FUN")
    def test_Morse_003(self):
        self.assertEqual(decoder.morse(".---- ..--- ...-- ....- ....."),"12345")
    def test_Morse_004(self):
        self.assertEqual(decoder.morse(".- .-. .. ..-. .. -.-. .. .- .-.. / .. -. - . .-.. .-.. .. --. . -. -.-. ."),"ARIFICIAL INTELLIGENCE")
    # XOR
    def test_XOR_001(self):
        self.assertEqual(decoder.xor(["23","00","15","07","0a","55","4b","32","16","19","09","1d","4a"],"key"), 'Hello, World!')
    def test_XOR_002(self):
        self.assertEqual(decoder.xor(["23","1c","17","1a","0a","1a","53","0c","10","52","03","01","1d"],"secret"), 'Python is fun')
    def test_XOR_003(self):
        self.assertEqual(decoder.xor(["33","0e","17","1a","19","08","52","0d","03","41","12","04","12","1c","1d","09","15"],"password"), 'Coding is awesome')
    def test_XOR_004(self):
        self.assertEqual(decoder.xor(["2c","0c","0d","23","10","1b","4b","26","16","1b","0c","15","04","11"],"key"), 'GitHub Copilot')
    def test_XOR_005(self):
        self.assertEqual(decoder.xor(["32","17","17","1b","03","1d","10","0c","02","1e","45","3d","1d","11","06","1e","09","1d","14","00","0d","11","00"],"secret"), 'Artificial Intelligence')
    # Base64
    def test_Base64_001(self):
        self.assertEqual(decoder.base64('SGVsbG8sIFdvcmxkIQ=='), 'Hello, World!')
    def test_Base64_002(self):
        self.assertEqual(decoder.base64('UGh5dG9uIGlzIGZ1bg=='), 'Python is fun')
    def test_Base64_003(self):
        self.assertEqual(decoder.base64('MTIzNDU='), '12345')
    def test_Base64_004(self):
        self.assertEqual(decoder.base64('QXJ0aWZpY2lhbCBJbnRlbGxpZWljaW5nZQ=='), 'Artificial Intelligence')
    def test_Base64_005(self):
        self.assertEqual(decoder.base64('R2l0SHViIENvcG9saXQ='), 'GitHub Copilot')