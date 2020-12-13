def check_bus(bus, n):
    multiples = []
    s = 0
    while True:
        s += bus
        if s > n:
            return s

def get_earliest_bus(buses, timestamp):
    earliest_bus = None
    earliest_time = 1000000000
    for bus in buses:
        earliest = check_bus(bus, timestamp)
        if earliest < earliest_time:
            earliest_time = earliest
            earliest_bus = bus
    return (earliest_time -timestamp) * earliest_bus

def bus_at_timestamp(bus, timestamp):
    q = int(timestamp / bus)
    return q * bus == timestamp

def get_earliest_timestamp_tc(buses):
    """
    My incomplete solution. It would work eventually
    but was taking too long. The only faster way to
    prune solutions I could think of was increment
    the timestamp by the biggest one, but it still wasn't
    fast enough.
    """
    timestamp = 0
    while True:
        success = True
        for bus, offset in buses:
            if not bus_at_timestamp(bus, timestamp + offset):
                success = False
                break
        if success:
            return timestamp
        timestamp += buses[0][0]
        timestamp -= buses[0][1]

def get_earliest_timestamp_crm(buses):
    """
    Solve the problem using the Chinese-remainder theorm.

    Credit: https://www.reddit.com/r/adventofcode/comments/kc5bl5/weird_math_trick_goes_viral/gfotzko/
    """
    increment = buses[0][0]
    pos = buses[0][1]
    for i in range(1, len(buses)):
        time, offset = buses[i]
        while (pos + offset) % time != 0:
            pos += increment

        increment *= time
    return pos


def part1():
    with open("puzzle", "r") as f:
        lines = f.readlines()
        timestamp = int(lines[0].strip())
        buses = []
        for bus in lines[1].strip().split(","):
            if bus != 'x':
                buses.append(int(bus))
        return get_earliest_bus(buses, timestamp)


def part2():
    with open("puzzle", "r") as f:
        lines = f.readlines()
        buses = []
        for offset, bus in enumerate(lines[1].strip().split(",")):
            if bus != 'x':
                buses.append((int(bus), offset))
        return get_earliest_timestamp_crm(buses)


if __name__ == '__main__':
    print part1()
    print part2()

