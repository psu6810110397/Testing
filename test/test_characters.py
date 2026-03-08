import unittest
from production.characters import alternatingCharacters


class TestAlternatingCharacters(unittest.TestCase):

    def test_alternating_characters_no_deletions(self):

        s = "ABABABAB"
        expected = 0

        result = alternatingCharacters(s)

        self.assertEqual(result, expected)

    def test_alternating_characters_all_same(self):

        s = "AAAA"
        expected = 3

        result = alternatingCharacters(s)

        self.assertEqual(result, expected)

    def test_alternating_characters_some_deletions(self):

        s = "AAABBB"
        expected = 4

        result = alternatingCharacters(s)

        self.assertEqual(result, expected)
