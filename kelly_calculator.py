

class calculator():

    def __init__(self, p, b, q):
        self.p = p
        self.b = b
        self.q = q

    def kelly_criterion(self):
        return (self.p * self.b - self.q) / self.b

    