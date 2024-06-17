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