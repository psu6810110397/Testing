import unittest
from unittest.mock import patch
from production.challenge import gridChallenge, run_with_input


class TestGridChallenge(unittest.TestCase):

    def test_grid_challenge_should_be_yes(self):

        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        expected = "YES"

        result = gridChallenge(grid)

        self.assertEqual(result, expected)

    def test_grid_challenge_should_be_no(self):

        grid = ["mpxz", "abcd", "wlmf"]
        expected = "NO"

        result = gridChallenge(grid)

        self.assertEqual(result, expected)

    def test_grid_challenge_single_row(self):

        grid = ["cba"]
        expected = "YES"

        result = gridChallenge(grid)

        self.assertEqual(result, expected)

    @patch("builtins.input", side_effect=["3", "mpxz", "abcd", "wlmf"])
    def test_run_with_input_using_stub(self, mock_input):

        expected = "NO"

        result = run_with_input()

        self.assertEqual(result, expected)
        self.assertEqual(mock_input.call_count, 4)

    def test_grid_challenge_empty_grid(self):
        # Arrange: กรณี Edge Case ที่สุดคือไม่มีข้อมูลในกริดเลย (Grid ว่าง)
        grid = []
        expected = "YES"

        # Act
        result = gridChallenge(grid)

        # Assert
        self.assertEqual(result, expected)
