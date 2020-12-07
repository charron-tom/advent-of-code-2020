from parser import RuleParser, Bag

def part1(sgb, tree):
    s = [sgb]
    visited = set()
    while s:
        b = s.pop()
        for outer, bags in tree.items():
            if b in bags and outer not in visited:
                s.append(outer)
                visited.add(outer)
    return len(visited)

def search(bag, tree):
    children = tree.get(bag, [])
    return bag.quantity + sum(child.quantity * search(Bag(child.bag_type), tree) for child in children)


def main():
    tree = dict()
    with open("puzzle", "r") as f:
        for line in f:
            tree.update(RuleParser.parse_rule(line.strip()))

    sgb = Bag("shiny gold")
    print part1(sgb, tree)
    print search(sgb, tree)


if __name__ == "__main__":
    main()
