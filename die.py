import random
from collections import defaultdict

class Die:
    def __init__(self):
        self.sides = ['D', 'D', 'D', 'L', 'R', 'C']

    def roll(self):
        return self.sides[random.randint(0, 5)]


# for debugging stuff
if __name__ == "__main__":
    d = Die()
    c = defaultdict(int)
    for i in range(1000):
        c[d.roll()] += 1

    print "D:", c['D']
    print "L:", c['L']
    print "R:", c['R']
    print "C:", c['C']