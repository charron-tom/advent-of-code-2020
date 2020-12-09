import copy

def check(n, num):
    for i in n:
        if num - i in n:
            return True
    return False


def part1():
    n = []
    preamble = 25
    with open("puzzle", "r") as f:
        for line in f:
            num = int(line.strip())
            if len(n) < preamble:
                n.append(num)
            elif len(n) == preamble:
                if not check(n, num):
                    return num
                n = n[1:]
                n.append(num)


def check_contiguous(start, n, total):
    s = 0
    end = copy.deepcopy(start)
    while s < total:
        s += n[end]
        if s == total:
            assert sum(n[start:end+1]) == total
            return n[start:end+1]
        elif s > total:
            return
        end += 1


def part2(total):
    n = []
    with open("puzzle", "r") as f:
        for line in f:
            n.append(int(line.strip()))
        for i,num in enumerate(n):
            r = check_contiguous(i, n, total)
            if r:
                return min(r) + max(r)


if __name__ == "__main__":
    total = part1()
    print total
    print part2(total)
