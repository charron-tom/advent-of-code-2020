from seatfinder import SeatFinder
def main():
    max_id = 0
    l = list()
    with open("puzzle", "r") as f:
        for line in f:
            seat = SeatFinder.get_seat(line.strip())
            max_id = max(max_id, seat.id)
            l.append(seat.id)

    l.sort()
    i = 0
    while i < len(l):
        if l[i+1] != l[i] + 1:
            return l[i] + 1
        i += 1


if __name__ == "__main__":
    print main()
