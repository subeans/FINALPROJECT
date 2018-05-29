import random

class StrikeBall:

    def __init__(self):
        self.secret = []
        self.digits = 0
        self.trials = 0

    def newGame(self, count):
        self.secret = []
        self.digits = count
        for i in range(self.digits):
            r = random.randint(1, 9)
            while r in self.secret:
                r = random.randint(1, 9)
            self.secret.append(r)
        self.trials = 0

    def guess(self, userGuess):
        self.trials += 1
        strikes, balls = 0, 0
        strikesSet = set()
        g = [int(x) for x in userGuess]
        for i in range(self.digits):
            if g[i] == self.secret[i]:
                strikes += 1
                strikesSet.add(g[i])
        for i in range(self.digits):
            if g[i] not in strikesSet and g[i] in self.secret:
                balls += 1
        return strikes, balls

    def getGuessCount(self):
        return self.trials


if __name__ == '__main__':
    s = StrikeBall()
    count = 3
    s.newGame(count)
    strikes = 0
    while strikes < count:
        inputString = input("Your guess: ")
        while len(inputString) != count:
            print("Input %d digits!" % count)
            inputString = input("Your guess: ")
        if inputString == "0" * count:
            print(s.secret)
        strikes, balls = s.guess(inputString)
        print("%d strike(s), %d ball(s)" % (strikes, balls))

    guessCount = s.getGuessCount()
    print("SUCCESS in %d trials" % guessCount)
