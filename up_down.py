import random

class UpDown:

    def __init__(self):
        self.ran = 0
        self.digits = 0
        self.trials = 0

    def newGame(self, count):
        self.ran = 0
        self.digits = count
	self.ran = random.randint(1,self.digits)
	self.trials =0
	       

    def updown(self, userGuess):
        self.trials += 1
	if self.ran > userGuess:
	       return "Greater"
	elif self.ran < userGuess:
	       return "Smaller"

    def getGuessCount(self):
        return self.trials


if __name__ == '__main__':
    s = UpDown()
    count = 80
    s.newGame(count)
    inputNum= -1
    while count!=inputNum:
        inputNum = int(input("Your guess:"))

        if inputNum == 0:
            print(s.ran)
        answer = s.guess(inputNum)
        print("%s" % answer)

    guessCount = s.getGuessCount()
    print("SUCCESS in %d trials" % guessCount)
