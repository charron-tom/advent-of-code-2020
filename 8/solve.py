import copy

class Instruction:
    def __init__(self, opcode, amt, id):
        self.opcode = opcode
        self.amt = amt
        self.id = id


def run_program(program):
    i = 0
    acc = 0
    visited = set()
    success = True
    while i < len(program):
        ins = program[i]
        if ins.id in visited:
            success = False
            break
        else:
            visited.add(ins.id)
        if ins.opcode == 'acc':
            if ins.amt[0] == '+':
                acc += int(ins.amt[1:])
            else:
                acc -= int(ins.amt[1:])
        elif ins.opcode == 'jmp':
            if ins.amt[0] == '+':
                i += int(ins.amt[1:])
            else:
                i -= int(ins.amt[1:])
            continue
        i += 1

    return success, acc

def main():
    with open("puzzle", "r") as f:
        computer = []
        for i, line in enumerate(f):
            opcode, amt = line.strip().split(" ")
            computer.append(Instruction(opcode, amt, i))

        for i in range(len(computer)):
            ins = computer[i]
            if ins.opcode == 'acc':
                continue
            cp = copy.deepcopy(computer)
            if cp[i].opcode == 'jmp':
                cp[i].opcode = 'nop'
            elif cp[i].opcode == 'nop':
                cp[i].opcode = 'jmp'
            success, acc = run_program(cp)
            if success:
                print acc
                break

if __name__ == "__main__":
    main()
