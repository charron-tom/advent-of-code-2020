import re
from passport import Passport

class PassportValidator:

    REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    @staticmethod
    def validate(passport):
        diff = PassportValidator.REQUIRED_FIELDS.intersection(passport.fields)
        is_valid = int(diff == PassportValidator.REQUIRED_FIELDS)
        if not is_valid:
            return False
        try:
            PassportValidator.validate_byr(passport.byr)
            PassportValidator.validate_iyr(passport.iyr)
            PassportValidator.validate_eyr(passport.eyr)
            PassportValidator.validate_hgt(passport.hgt)
            PassportValidator.validate_hcl(passport.hcl)
            PassportValidator.validate_ecl(passport.ecl)
            PassportValidator.validate_pid(passport.pid)
            return True
        except ValueError as e:
            return False


    @staticmethod
    def validate_byr(byr):
        if int(byr) < 1920 or int(byr) > 2002:
            raise ValueError('byr', byr)

    @staticmethod
    def validate_iyr(iyr):
        if int(iyr) < 2010 or int(iyr) > 2020:
            raise ValueError('iyr', iyr)

    @staticmethod
    def validate_eyr(eyr):
        if int(eyr) < 2020 or int(eyr) > 2030:
            raise ValueError('eyr', eyr)

    @staticmethod
    def validate_hgt(hgt):
        match = re.match(r"(\d+)(in|cm)", hgt)
        if match:
            unit = match.group(2)
            height = int(match.group(1))
            if unit == "cm":
                if height < 150 or height > 193:
                    raise ValueError('hgt', height)
            elif unit == "in":
                if height < 59 or height > 76:
                    raise ValueError('hgt', height)
        else:
            raise ValueError('hgt', hgt)

    @staticmethod
    def validate_hcl(hcl):
        if not re.match(r"#[0-9a-f]{6}$", hcl):
            raise ValueError('hcl', hcl)

    @staticmethod
    def validate_ecl(ecl):
        if not re.match(r"amb|blu|brn|gry|grn|hzl|oth$", ecl):
            raise ValueError('ecl', ecl)

    @staticmethod
    def validate_pid(pid):
        if not re.match(r"\d{9}$", pid):
            raise ValueError('pid', pid)


def main():
    count = 0
    with open("puzzle", "r") as f:
        p = Passport()
        for line in f:
            if line.strip():
                p.update(line.strip().split(" "))
            else:
                count += int(PassportValidator.validate(p))
                p = Passport()
        count += int(PassportValidator.validate(p))
    return count

if __name__ == '__main__':
    print main()
