class Field:
    def __init__(self, name, r1, r2):
        self.name = name
        self.range1 = r1
        self.range2 = r2
        self.index = None

    def __eq__(self, o):
        return self.name == o.name and self.range1 == o.range1 and self.range2 == o.range2

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"
