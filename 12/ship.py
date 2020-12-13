import math

class Navigatable:

    def __init__(self, x=None, y=None):
        self._x = x or 0
        self._y = y or 0

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y

    def north(self, y):
        self._y += y

    def south(self, y):
        self._y -= y

    def east(self, x):
        self._x += x

    def west(self, x):
        self._x -= x


class Ship(Navigatable):
    def __init__(self):
        super().__init__()
        self.heading = 90 # start by facing east

    def left(self, deg):
        self.heading -= deg
        self.heading = self.heading % 360

    def right(self, deg):
        self.heading += deg
        self.heading = self.heading % 360

    def forward(self, amt):
        rad = math.radians(self.heading)
        self._x += (round(math.sin(rad), 2) * amt)
        self._y += (round(math.cos(rad), 2) * amt)


    def distance(self):
        return abs(self.x) + abs(self.y)

    def __str__(self):
        return '({},{}) heading {}'.format(self.x, self.y, self.heading)

class Waypoint(Navigatable):
    def __init__(self, ship):
        super().__init__(x=10, y=1)
        self.ship = ship

    @property
    def x(self):
        return self.ship.x + self._x

    @property
    def y(self):
        return self.ship.y + self._y

    def left(self, deg):
        if deg == 270:
            return self.right(90)
        if deg == 180:
            self._x, self._y = -self._x, -self._y
        elif deg == 90:
            self._x, self._y = -self._y, self._x

    def right(self, deg):
        if deg == 270:
            return self.left(90)
        if deg == 180:
            self._x, self._y = -self._x, -self._y
        elif deg == 90:
            self._x, self._y = self._y, -self._x

    def forward(self, amt):
        for _ in range(amt):
            self.ship.x += self._x
            self.ship.y += self._y


    def __str__(self):
        return '({},{}) relative to ship'.format(self.x - self.ship.x, self.y - self.ship.y)



def move(n, ins):
    code = ins[0]
    amt = int(ins[1:])
    if code == 'L':
        return n.left(amt)
    if code == 'R':
        return n.right(amt)
    if code == 'N':
        return n.north(amt)
    if code == 'E':
        return n.east(amt)
    if code == 'S':
        return n.south(amt)
    if code == 'W':
        return n.west(amt)
    if code == 'F':
        return n.forward(amt)
