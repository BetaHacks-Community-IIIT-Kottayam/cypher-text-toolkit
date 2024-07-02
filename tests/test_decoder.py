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