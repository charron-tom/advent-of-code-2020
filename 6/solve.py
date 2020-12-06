from group import Group


def main():
    with open("puzzle", "r") as f:
        g = Group()
        c = 0
        for line in f:
            person = line.strip()
            if person:
                g.add_person(person)
            else:
                c += g.find_questions()
                g = Group()
        c += g.find_questions()
        return c

if __name__ == "__main__":
    print main()
