from enum import Enum


class SeatState(Enum):
    EMPTY = 1
    OCCUPIED = 2
    FLOOR = 3


class Seat:
    def __init__(self, state, i, j):
        self.state = state
        self.next_state = state
        self.i = i
        self.j = j
        self.neighbors = []

    @property
    def is_occupied(self):
        return self.state == SeatState.OCCUPIED

    @property
    def seatable(self):
        return self.state == SeatState.EMPTY or self.state == SeatState.OCCUPIED


    def compute_next_state(self, grid, max_occupied):
        if not self.seatable:
            self.next_state = SeatState.FLOOR
        if self.state == SeatState.EMPTY:
            self.next_state = self._compute_next_empty()
        elif self.state == SeatState.OCCUPIED:
            self.next_state = self._compute_next_occupied(max_occupied)

    def switch(self):
        self.state = self.next_state
        self.next_state = self.next_state

    def _compute_next_empty(self):
        next_state = SeatState.OCCUPIED
        for seat in self.neighbors:
            if seat.is_occupied:
                next_state = SeatState.EMPTY
                break
        return next_state

    def _compute_next_occupied(self, max_occupied):
        occupied_seats = 0
        for seat in self.neighbors:
            if seat.is_occupied:
                occupied_seats += 1
        next_state = SeatState.OCCUPIED
        if occupied_seats >= max_occupied:
            next_state = SeatState.EMPTY
        return next_state

    def __repr__(self):
        if not self.seatable:
            return '.'
        return '#' if self.is_occupied else 'L'

    def __str__(self):
        if not self.seatable:
            return '.'
        return '#' if self.is_occupied else 'L'

def find_neighbors(seat, grid):
    coords = [(seat.i-1, seat.j),
              (seat.i-1, seat.j+1),
              (seat.i, seat.j+1),
              (seat.i+1, seat.j+1),
              (seat.i+1, seat.j),
              (seat.i+1, seat.j-1),
              (seat.i, seat.j-1),
              (seat.i-1, seat.j-1)]

    neighbors = []
    for i, j in coords:
        try:
            # no negative indicies in this puzzle
            if (i >= 0) and (j >= 0) and grid[i][j].seatable:
                neighbors.append(grid[i][j])
        except IndexError:
            pass
    return neighbors


def find_neighbors_endless(seat, grid):
    def search(i_fn, j_fn):
        try:
            i = i_fn(seat.i)
            j = j_fn(seat.j)
            neighbor = grid[i][j]
            while not neighbor.seatable and (i_fn(i) >= 0 and j_fn(j) >= 0):
                i = i_fn(i)
                j = j_fn(j)
                neighbor= grid[i][j]
            if neighbor.seatable and (i >= 0) and (j >= 0):
                return neighbor
        except IndexError:
            return

    coords = [(lambda i: i-1, lambda j: j),
              (lambda i: i-1, lambda j: j+1),
              (lambda i: i, lambda j: j+1),
              (lambda i: i+1, lambda j: j+1),
              (lambda i: i+1, lambda j: j),
              (lambda i: i+1, lambda j: j-1),
              (lambda i: i, lambda j: j-1),
              (lambda i: i-1, lambda j: j-1)]

    neighbors = []
    for index, coord in enumerate(coords):
        i_fn, j_fn = coord
        neighbor = search(i_fn, j_fn)
        if neighbor:
            neighbors.append(neighbor)
    return neighbors


def get_seat_state(char):
    if char == '.':
        return SeatState.FLOOR
    elif char == 'L':
        return SeatState.EMPTY
    raise ValueError('cannot derive SeatState from ', char)
