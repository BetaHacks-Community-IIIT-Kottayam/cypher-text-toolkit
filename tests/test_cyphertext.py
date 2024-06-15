#!/usr/bin/env python

"""Tests for `cyphertext` package."""


import unittest

from cyphertext.encoder import *


class TestCyphertext(unittest.TestCase):
    """Tests for `cyphertext` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
    # caesar
    def test_Caesar_001(self):
        self.assertEqual(caesar('Hello, World!', 3), 'KHOOR, ZRUOG!')
    def test_Caesar_002(self):
        self.assertEqual(caesar('Hello, World!', 0), 'HELLO, WORLD!')
    def test_Caesar_003(self):
        self.assertEqual(caesar('Hello, World!', 26), 'HELLO, WORLD!')
    def test_Caesar_004(self):
        self.assertEqual(caesar('Hello, World!', 27), 'IFMMP, XPSME!')
    def test_Caesar_005(self):
        self.assertEqual(caesar('Hello, World!', 128), 'FCJJM, UMPJB!')
    def test_Caesar_006(self):
        self.assertEqual(caesar('Hello, World!', -3), 'EBIIL, TLOIA!')
    # Piglatin
    def test_Piglatin_001(self):
        self.assertEqual(piglatin('Hello, World!'), 'elloHay, orldWay!')
    def test_Piglatin_002(self):
        self.assertEqual(piglatin('Python is fun'), 'ythonPay isay unfay')
    def test_Piglatin_003(self):
        self.assertEqual(piglatin('Coding is awesome'), 'odingCay isay awesomay')
    def test_Piglatin_004(self):
        self.assertEqual(piglatin('GitHub Copilot'), 'itHubGay opilotCay')
    def test_Piglatin_005(self):
        self.assertEqual(piglatin('Artificial Intelligence'), 'Artificialay Intelligenceay')
