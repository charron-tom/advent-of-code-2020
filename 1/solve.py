def find(nums, total):
    for n in nums:
        if total - n in nums:
            return n, total - n

def main():
    with open("puzzle", "r") as f:
        nums = set()
        for l in f:
            nums.add(int(l.strip()))
        for n in nums:
            res = find(nums, 2020 - n)
            if res is not None:
                return res[0] * res[1] * n

if __name__ == '__main__':
    print main()
