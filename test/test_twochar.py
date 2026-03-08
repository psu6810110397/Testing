import unittest
from production.twochar import alternate


class TestTwoCharacters(unittest.TestCase):

    def test_alternate_longest_valid_string(self):

        s = "beabeefeab"
        expected = 5

        result = alternate(s)

        self.assertEqual(result, expected)

    def test_alternate_no_valid_pair(self):

        s = "a"
        expected = 0

        result = alternate(s)

        self.assertEqual(result, expected)

    def test_alternate_all_same_characters(self):

        s = "aaaa"
        expected = 0

        result = alternate(s)

        self.assertEqual(result, expected)

    def test_alternate_already_perfect_alternating(self):

        s = "xyxyxy"
        expected = 6

        result = alternate(s)

        self.assertEqual(result, expected)
