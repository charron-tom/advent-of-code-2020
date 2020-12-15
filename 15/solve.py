class TruncatedList(list):
    """
    Special child class of list to only hold a specified
    number of items.
    """

    def __init__(self, max_size):
        self.max_size = max_size
        super().__init__()

    def append(self, item):
        if len(self) == self.max_size:
            self.pop(0)
        list.append(self, item)


class Game(dict):
    """
    The game class.
    """

    def __init__(self, start):
        self.turn = 1
        for n in start:
            self[n].append(self.turn)
            self.turn += 1

    def __getitem__(self, key):
        """
        Override this method so we can use `TruncatedList` so
        we don't store unecessary data.
        """
        if key not in self:
            self[key] = TruncatedList(2)
        return dict.__getitem__(self, key)

    def speak_number(self, last_spoken):
        """
        Speak the next number.
        """
        if len(self[last_spoken]) == 1:
            speak = 0
        else:
            speak = self[last_spoken][-1] - self[last_spoken][-2]
        self[speak].append(self.turn)
        return speak


def play_game(starting_num, n):
    """
    Play the game with `starting_num` in `n` turns.
    """
    g = Game(starting_num)
    last_spoken = starting_num[-1]
    while g.turn <= n:
        last_spoken = g.speak_number(last_spoken)
        g.turn += 1

    return last_spoken



if __name__ == '__main__':
    print play_game([5,2,8,16,18,0,1], 2020)
    print play_game([5,2,8,16,18,0,1], 30000000)
