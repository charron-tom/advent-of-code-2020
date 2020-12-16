from field import Field


def get_fields():
    """
    Parse a list of `Field` objects out of the file.
    """
    fields = []
    with open("rules", "r") as f:
        for line in f:
            field, ranges = line.strip().split(": ")
            r1, r2 = ranges.split(" or ")
            range1 = get_range(r1)
            range2 = get_range(r2)
            fields.append(Field(field, range1, range2))
    return fields


def get_range(s):
    """
    Return an actual `range` object from an input string.
    """
    r = s.split("-")
    return range(int(r[0]), int(r[1]) + 1)

