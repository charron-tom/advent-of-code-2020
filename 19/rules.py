class Rule:

    def __init__(self, *args):
        self.deps = []
        for arg in args:
            self.deps.append(arg)

    def resolve(self, m):
        msg = ""
        for dep in self.deps:
            if dep not in m:
                msg += dep[1]
            else:
                msg += m.get(dep).resolve(m)
        return "(" + msg + ")"

    @staticmethod
    def create(r):
        if "|" in r:
            r1, r2 = r.split(" | ")
            return OrRule(Rule(*r1.split(" ")), Rule(*r2.split(" ")))
        return Rule(*r.split(" "))


class OrRule(Rule):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def resolve(self, m):
        return "(" + self.left.resolve(m) + "|" + self.right.resolve(m) + ")"


class RepeatingRule(Rule):

    def __init__(self, repeat):
        self.repeat = repeat

    def resolve(self, m):
        return "(" + self.repeat.resolve(m) + ")+"


class RecursiveRule(Rule):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def resolve(self, m):
        return "(?<rec>" + self.left.resolve(m) + "(?&rec)?" + self.right.resolve(m) + ")"


def get_rules():
    rules = {}
    with open("rules.txt") as f:
        for line in f:
            n, rule = line.split(": ")
            rules[n] = Rule.create(rule.strip())
    return rules
