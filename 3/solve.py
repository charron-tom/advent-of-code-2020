class DownSlope(object):
    def __init__(self, right, down):
        self.right = right
        self.down = down

    def check_puzzle(self, puzzle):
        j = 0
        trees = 0
        for i in range(self.down, len(puzzle) - 1, self.down):
            line_size = len(puzzle[i])
            j += self.right
            j = j % line_size
            if puzzle[i][j] == '#':
                trees += 1
        return trees


class Down1Slope(DownSlope):
    def __init__(self, right):
        super(Down1Slope, self).__init__(right, 1)


class Down2Slope(DownSlope):
    def __init__(self, right):
        super(Down2Slope, self).__init__(right, 2)


def main():
    with open("puzzle", "r") as f:
        puzzle = [l.strip() for l in f.readlines()]
        slopes = [Down1Slope(1), Down1Slope(3), Down1Slope(5), Down1Slope(7), Down2Slope(1)]
        s = 1
        for slope in slopes:
            s *= slope.check_puzzle(puzzle)
        return s


if __name__ == '__main__':
    print main()
