class PasswordPolicy:
    
    def __init__(self, min, max, char):
        self.min = int(min)
        self.max = int(max)
        self.char = char

    def test_password(self, password):
        freq = password.count(self.char)
        if freq >= self.min and freq <= self.max:
            return True
        return False

    def test_password_adv(self, password):
        s = ""
        s += password[self.min -1]
        s += password[self.max - 1]
        return s.count(self.char) == 1

def main():
    count = 0
    with open("puzzle", "r") as f:
        for line in f:
            l = line.strip()
            policy, password = l.split(": ")
            freq, char = policy.split(" ")
            min_freq, max_freq = freq.split("-")
            p = PasswordPolicy(min_freq, max_freq, char)
            if p.test_password_adv(password):
                count += 1
    return count


if __name__ == '__main__':
    print main()
