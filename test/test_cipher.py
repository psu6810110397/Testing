import unittest
from production.cipher import caesarCipher


class TestCaesarCipher(unittest.TestCase):

    def test_caesar_cipher_lowercase_and_wrap(self):

        s = "xyz"
        k = 3
        expected = "abc"

        result = caesarCipher(s, k)

        self.assertEqual(result, expected)

    def test_caesar_cipher_uppercase_and_special_chars(self):

        s = "Hello-World!"
        k = 2
        expected = "Jgnnq-Yqtnf!"

        result = caesarCipher(s, k)

        self.assertEqual(result, expected)

    def test_caesar_cipher_large_k(self):

        s = "abc"
        k = 28
        expected = "cde"

        result = caesarCipher(s, k)

        self.assertEqual(result, expected)
