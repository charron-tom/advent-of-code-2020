class Seat:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.id = (row * 8) + column

    def __eq__(self, o):
        return self.row == o.row and self.column == o.column and self.id == o.id


class SeatFinder:

    @staticmethod
    def get_seat(code):
        row = SeatFinder.get_row(code[:7])
        column = SeatFinder.get_column(code[-3:])
        return Seat(row, column)

    @staticmethod
    def get_column(code):
        if len(code) != 3:
            raise ValueError("code must be exactly 3 chars")
        r = range(8)
        while code != "":
            r = bin_helper(r, code[0])
            code = code[1:]
        return r[0]
        

    @staticmethod
    def get_row(code):
        if len(code) != 7:
            raise ValueError("code must be exactly 7 chars")

        r = range(128)
        while code != "":
            r = bin_helper(r, code[0])
            code = code[1:]
        return r[0]


def bin_helper(r, letter):
    if letter == 'F' or letter == 'L':
        return r[:len(r)/2]
    elif letter == 'B' or letter == 'R':
        return r[len(r)/2:]
