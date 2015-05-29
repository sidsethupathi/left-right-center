from player import Player
from die import Die
from collections import defaultdict
import sys

class Game:
    def __init__(self, count, start):
        self.count = count
        self.players = [Player(i) for i in xrange(count)]
        self.die = Die()
        self.start = start

    def checkGameOver(self):
        winner = None
        for i in self.players:
            if i.chips == 0:
                pass
            else:
                if winner == None:
                    winner = i.id
                elif winner != None:
                    return None
        return winner

    def displayChipCount(self):
        print '{',
        for p in self.players:
            print str(p.id) + ':' + str(p.chips) +  ' |',
        print '}'

    def play(self):
        current = self.start
        winner = self.checkGameOver()
        while winner == None:
            L = (current - 1) % self.count
            R = (current + 1) % self.count

            #make moves in order
            if self.players[current].chips > 3:
                rolls = 3
            else:
                rolls = self.players[current].chips

            for i in range(rolls):
                move = self.die.roll()
                if move == 'D':
                    pass
                elif move == 'L':
                    self.players[L].add()
                    self.players[current].remove()
                elif move == 'R':
                    self.players[R].add()
                    self.players[current].remove()
                elif move == 'C':
                    self.players[current].remove()

            current = (current + 1) % self.count
            winner = self.checkGameOver()

        return winner


if __name__ == "__main__":
    player_count = int(sys.argv[1])
    num_tests = int(sys.argv[2])
    c = defaultdict(int)

    winner = 0
    for i in range(num_tests):
        g = Game(player_count, winner)
        winner = g.play()
        c[winner] += 1

    print "After", num_tests, "games..."
    for p in c:
        print "Player", p, "wins: ", c[p]
    