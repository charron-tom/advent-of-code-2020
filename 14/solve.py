from mask import AddressMask, ValueMask
from memory import Memory


def main():
    mem = Memory()
    mem2 = Memory()
    with open("puzzle", "r") as f:
        for line in f:
            if "mask" in line:
                mem.mask = ValueMask.create(line.strip().split(" = ")[1])
                mem2.mask = AddressMask.create(line.strip().split(" = ")[1])
            else:
                exec(line.strip())
                exec(line.strip().replace("mem", "mem2"))

    print mem.sum()
    print mem2.sum()


if __name__ == '__main__':
    main()
