class Puppet:
    def __init__(self):
        self.bodyParts = self.buildBodyParts()

    def buildBodyParts(self):
        return {
            "head": {
                "status": True,
                "asset": ""
            },
            "torso": {
                "status": True,
                "asset": ""
            },
            "rightArm": {
                "status": True,
                "asset": ""
            },
            "leftArm": {
                "status": True,
                "asset": ""
            },
            "rightLeg": {
                "status": True,
                "asset": ""
            },
            "leftLeg": {
                "status": True,
                "asset": ""
            },
        }
    
    def tryGotWrong(self):
        i = self.countRemainingParts()
        self.bodyPartRemover()
        if i > 1:
            pass
        else:
            pass

    

    def countRemainingParts(self):
        for key, value in self.bodyParts:
            if value.status:
                i += 1
        return i

    def bodyPartRemover(self):
        for key, value in self.bodyParts:
            if value.status:
                status = False
                break
        
           






class Game:
    def __init__(self):
        self.word = ""
        self.words = ["gabriel",]
        self.defineChoosenWord()
        self.pannel = self.resetPannel()

    def defineChoosenWord(self):
        self.word = self.words[0]
    
    def resetPannel(self):
        return [" " for c in range(len(self.word))]
    
    def handleTry(self, letterTried):
        if (self.isLetterPresent(letterTried)): # Esse código roda quando o usuário acerta
            self.updatePannel(letterTried)
            self.handleVictory()


    def isLetterPresent(self, letter):
        for e, l in enumerate(self.word):
            if l == self.word[e]:
                return True
        return False
    
    def updatePannel(self, letterTried):
        for e, l in enumerate(self.word):
            if letterTried == self.word[e]:
                self.pannel[e] = letterTried

    def hasVictoryHappen(self):
        for l in self.pannel:
            if l == " ":
                return False
        return True

    def handleVictory(self):
        if self.hasVictoryHappen():
            msg = "Você venceu!!"
            size = len(msg) + 4
            print("=" * (len(msg) + 4))
            print(f"  {msg}  ")
            print("=" * (len(msg) + 4))
            self.pannel = self.resetPannel()

class Test:
    def __init__(self):
        pass
    def testGame(self, gameInstance):
        while True:
            print(gameInstance.pannel)
            guess = input("Chute uma letra:")
            gameInstance.handleTry(guess)


gameInstance = Game()
testInstance = Test() 
testInstance.testGame(gameInstance)