import copy

from utils import get_fields, get_range


def part1():
    n = set()
    fields = get_fields()
    for field in fields:
        n.update(field.range1)
        n.update(field.range2)

    errors = 0
    valid_tickets = []
    with open("nearby", "r") as f:
        for line in f:
            valid_ticket = True
            for v in line.strip().split(","):
                if int(v) not in n:
                    errors += int(v)
                    valid_ticket = False
            if valid_ticket:
                valid_tickets.append(line.strip())

    return valid_tickets, errors

def find_fields(valid_tickets):
    solution = []
    fields = get_fields()
    for i in range(len(fields)):
        solution.append(copy.deepcopy(fields))

    for ticket in valid_tickets:
        for i,v in enumerate(ticket.split(",")):
            fields = []
            for field in solution[i]:
                if int(v) in field.range1 or int(v) in field.range2:
                    field.index = i
                    fields.append(field)
            solution[i] = fields

    solution = sorted(solution, key=lambda n: len(n))


    current_field = solution[0][0]
    final = []
    i = 0
    while i < len(solution) - 1:
        for j in range(i + 1, len(solution)):
            if current_field in solution[j]:
                solution[j].remove(current_field)
        i += 1
        current_field = solution[i][0]
        if "departure" in current_field.name:
            final.append(current_field)
    return final


def part2(valid_tickets):
    final = find_fields(valid_tickets)
    with open("ticket", "r") as f:
        ticket = f.readlines()[0].strip().split(",")
        q = 1
        for field in final:
            q *= int(ticket[field.index])
        return q


def main():
    valid_tickets, errors = part1()
    print(errors)
    print(part2(valid_tickets))


if __name__ == "__main__":
    main()
