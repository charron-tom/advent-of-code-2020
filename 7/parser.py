import re

class Bag:
    def __init__(self, bag_type, quantity=None):
        self.bag_type = bag_type
        if quantity:
            self.quantity = int(quantity)
        else:
            self.quantity = 1

    def __hash__(self):
        return hash(self.bag_type)

    def __eq__(self, o):
        return self.bag_type == o.bag_type


class RuleParser:

    @staticmethod
    def parse_rule(rule):
        b = re.match(r"(\w+\s\w+)\sbags contain (.*)", rule)
        bag = Bag(b.group(1))
        r = {bag: []}
        dependencies = b.group(2).split(", ")
        for dep in dependencies:
            m = re.match(r"(\d+)\s(\w+\s\w+)\sbag", dep)
            if m:
                r[bag].append(Bag(m.group(2), quantity=m.group(1)))
        return r
