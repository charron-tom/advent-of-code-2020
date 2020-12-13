from ship import Ship, Waypoint, move

def part1():
    ship = Ship()
    with open("puzzle", "r") as f:
        for line in f:
            move(ship, line.strip())
        return ship.distance()

def part2():
    ship = Ship()
    wp = Waypoint(ship)
    with open("puzzle", "r") as f:
        for line in f:
            move(wp, line.strip())
        return ship.distance()



if __name__ == '__main__':
    print part1()
    print part2()

