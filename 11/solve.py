from seat import (
    Seat,
    SeatState,
    find_neighbors,
    find_neighbors_endless,
    get_seat_state,
)


def build_grid():
    grid = []
    with open("puzzle", "r") as f:
        for i, line in enumerate(f):
            row = []
            for j, char in enumerate(line.strip()):
                state = get_seat_state(char)
                row.append(Seat(get_seat_state(char), i, j))
            grid.append(row)

        for row in grid:
            for seat in row:
                seat.neighbors = find_neighbors_endless(seat, grid)
    return grid

def run(grid, max_occupied):
    occupied = 0
    for row in grid:
        for seat in row:
            seat.compute_next_state(grid, max_occupied)
            if seat.next_state == SeatState.OCCUPIED:
                occupied += 1

    for row in grid:
        for seat in row:
            seat.switch()

    return occupied


def main():
    grid = build_grid()
    num_occupied = []
    n = 5 
    while True:
        occupied = run(grid, n)
        num_occupied.append(occupied)
        if sum(num_occupied[-n:]) / n == occupied:
            break
    return occupied


if __name__ == "__main__":
    print main()
