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
    def test_shift_001(self):
        self.assertEqual(ascii_shift("Hello, World!", 3), 'Khoor/#Zruog$')
    def test_shift_002(self):
        self.assertEqual(ascii_shift("Hello, World!", 0), 'Hello, World$')
    def test_shift_003(self):
        self.assertEqual(ascii_shift("Hello, World!", 26), 'Gdkkn/#Vnqkc$')
    def test_shift_004(self):
        self.assertEqual(ascii_shift("Hello, World!", 27), 'Ifmmp/#Xpsme$')
    def test_shift_005(self):
        self.assertEqual(ascii_shift("Hello, World!", 128), 'Hello, World$')
    def test_shift_006(self):
        self.assertEqual(ascii_shift("Hello, World!", -3), 'Ebiil/#Tloia$')
