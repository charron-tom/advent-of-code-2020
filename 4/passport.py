import json

class Passport:

    def __init__(self):
        self.passport = dict()

    @property
    def fields(self):
        return set(self.passport.keys())

    @property
    def byr(self):
        return self.passport["byr"]

    @property
    def iyr(self):
        return self.passport["iyr"]

    @property
    def eyr(self):
        return self.passport["eyr"]

    @property
    def hgt(self):
        return self.passport["hgt"]

    @property
    def hcl(self):
        return self.passport["hcl"]

    @property
    def ecl(self):
        return self.passport["ecl"]

    @property
    def pid(self):
        return self.passport["pid"]

    def update(self, passport_data):
        for data in passport_data:
            field, value = data.split(":")
            self.passport[field] = value

    def __str__(self):
        return json.dumps(self.passport)
