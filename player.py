class Player:
    def __init__(self, id):
        self.id = id
        self.chips = 3

    def add(self):
        self.chips += 1
        return True

    def remove(self):
        if self.chips != 0:
            self.chips -= 1
            return True
        else:
            return False

    def say(self):
        print "Player", self.id, "has", self.chips, "chips"

if __name__ == "__main__":
    p = Player()

    p.say()
    p.add()
    p.say()
    p.remove()
    p.say()
