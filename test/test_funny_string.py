import unittest
from production.funny_string import funnyString


class TestFunnyString(unittest.TestCase):

    def test_give_acxz_should_be_funny(self):

        s = "acxz"
        expected_output = "Funny"

        result = funnyString(s)

        self.assertEqual(result, expected_output)

    def test_give_bcxz_should_not_be_funny(self):

        s = "bcxz"
        expected_output = "Not Funny"

        result = funnyString(s)

        self.assertEqual(result, expected_output)
