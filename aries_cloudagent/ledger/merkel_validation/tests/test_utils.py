"""Tests for Merkel Validation Utils."""

from unittest import TestCase

from ..utils import ascii_chr, encode_hex


class TestUtils(TestCase):
    """Merkel Validation Utils Tests"""

    def test_encode_hex(self):
        assert encode_hex("test")
        with self.assertRaises(TypeError):
            encode_hex(123)

    def test_aschii_chr(self):
        assert ascii_chr(16 * 5 + 6)
