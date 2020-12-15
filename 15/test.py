import unittest

from solve import play_game

class TestGame(unittest.TestCase):

    def test_part1(self):
        """ Test the part1 solution. """
        self.assertEqual(play_game([0, 3, 6], 2020), 436)
        self.assertEqual(play_game([1, 3, 2], 2020), 1)
        self.assertEqual(play_game([2, 1, 3], 2020), 10)
        self.assertEqual(play_game([1, 2, 3], 2020), 27)
        self.assertEqual(play_game([2, 3, 1], 2020), 78)
        self.assertEqual(play_game([3, 2, 1], 2020), 438)
        self.assertEqual(play_game([3, 1, 2], 2020), 1836)

    def test_part2(self):
        """ Test the part2 solution. WARNING - slow. """
        self.assertEqual(play_game([0, 3, 6], 30000000), 175594)
        self.assertEqual(play_game([1, 3, 2], 30000000), 2578)
        self.assertEqual(play_game([2, 1, 3], 30000000), 3544142)
        self.assertEqual(play_game([1, 2, 3], 30000000), 261214)
        self.assertEqual(play_game([2, 3, 1], 30000000), 6895259)
        self.assertEqual(play_game([3, 2, 1], 30000000), 18)
        self.assertEqual(play_game([3, 1, 2], 30000000), 362)

if __name__ == "__main__":
    unittest.main()
