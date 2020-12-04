import unittest
from solve import PassportValidator


class PassportValidatorTest(unittest.TestCase):

    def test_validate_byr(self):
        self.assertRaises(ValueError, PassportValidator.validate_byr, "2003")
        PassportValidator.validate_byr("2002")

    def test_validate_hgt(self):
        self.assertRaises(ValueError, PassportValidator.validate_hgt, "190in")
        self.assertRaises(ValueError, PassportValidator.validate_hgt, "190")
        PassportValidator.validate_hgt("60in")
        PassportValidator.validate_hgt("190cm")

    def test_validate_ecl(self):
        self.assertRaises(ValueError, PassportValidator.validate_ecl, "wat")
        self.assertRaises(ValueError, PassportValidator.validate_ecl, "bry")
        PassportValidator.validate_ecl("brn")

    def test_validate_pid(self):
        self.assertRaises(ValueError, PassportValidator.validate_pid, "0123456789")
        PassportValidator.validate_pid("000000001")


if __name__ == '__main__':
    unittest.main()
