from rules import RepeatingRule, RecursiveRule, Rule, get_rules
import regex as re


def _solve(rules):
    r = re.compile(rules.get("0").resolve(rules) + "$")
    s = 0
    with open("messages.txt", "r") as f:
        for line in f:
            if r.match(line.strip()):
                s += 1
    return s


def part_1():
    rules = get_rules()
    return _solve(rules)


def part_2():
    rules = get_rules()
    rules["8"] = RepeatingRule(Rule("42"))
    rules["11"] = RecursiveRule(Rule("42"), Rule("31"))
    return _solve(rules)


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
