class Group:

    def __init__(self):
        self.questions = {}
        self.size = 0

    def add_person(self, person):
        self.size += 1
        for c in person:
            if c not in self.questions:
                self.questions[c] = 0 
            self.questions[c] += 1

    def find_questions(self):
        c = 0
        for v in self.questions.values():
            if v == self.size:
                c += 1
        return c
