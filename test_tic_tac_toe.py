import unittest
from unittest.mock import patch
import tic_tac_toe_game as game


class TestTicTacToeGame(unittest.TestCase):

    def test_check_setup_for_tests(self):
        self.assertEqual(1 + 1, 2)

    def test_if_player_1_selects_0_as_marker_player_2_gets_X_as_marker_and_vice_versa(self):
        with patch('builtins.input', return_value='0'):
            result = game.get_valid_markers()
        self.assertListEqual(['0', 'X'], result)

        with patch('builtins.input', return_value='X'):
            result = game.get_valid_markers()
        self.assertListEqual(['X', '0'], result)


if __name__ == '__main__':
    unittest.main()
