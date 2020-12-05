import unittest
from seatfinder import Seat, SeatFinder, bin_helper

class SeatTest(unittest.TestCase):

    def test_find_seat(self):
        self.assertEqual(SeatFinder.get_seat("BFFFBBFRRR"), Seat(70, 7))
        self.assertEqual(SeatFinder.get_seat("FFFBBBFRRR"), Seat(14, 7))
        self.assertEqual(SeatFinder.get_seat("BBFFBBFRLL"), Seat(102, 4))

    def test_get_row(self):
        self.assertRaises(ValueError, SeatFinder.get_row, "BFFFBBFRRR")
        self.assertEqual(SeatFinder.get_row("BFFFBBF"), 70)
        self.assertEqual(SeatFinder.get_row("FFFBBBF"), 14)
        self.assertEqual(SeatFinder.get_row("BBFFBBF"), 102)

    def test_get_column(self):
        self.assertRaises(ValueError, SeatFinder.get_column, "BFFFBBFRRR")
        self.assertEqual(SeatFinder.get_column("RRR"), 7)
        self.assertEqual(SeatFinder.get_column("RRR"), 7)
        self.assertEqual(SeatFinder.get_column("RLL"), 4)


class TestBinHelper(unittest.TestCase):

    def test_bin_helper_row(self):
        self.assertEqual(bin_helper(range(128), "F"), range(64))
        self.assertEqual(bin_helper(range(64), "B"), range(32, 64))
        self.assertEqual(bin_helper(range(32, 64), "F"), range(32, 48))
        self.assertEqual(bin_helper(range(32, 48), "B"), range(40, 48))
        self.assertEqual(bin_helper(range(40, 48), "B"), range(44, 48))
        self.assertEqual(bin_helper(range(44, 48), "F"), range(44, 46))
        self.assertEqual(bin_helper(range(44, 46), "F"), range(44, 45))

    def test_bin_helper_col(self):
        self.assertEqual(bin_helper(range(8), "R"), range(4, 8))
        self.assertEqual(bin_helper(range(4, 8), "L"), range(4, 6))
        self.assertEqual(bin_helper(range(4, 6), "R"), range(5, 6))


if __name__ == '__main__':
    unittest.main()
