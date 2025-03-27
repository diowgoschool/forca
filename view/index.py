import pygame
import random  # Import random for selecting a random word

class Puppet:
    def __init__(self):
        self.bodyParts = self.buildBodyParts()

    def buildBodyParts(self):
        return {
            "head": {
                "status": True,
                "asset": "forca/assets/puppet/01_cabeça.png",
                "sprite": ""
            },
            "torso": {
                "status": True,
                "asset": "forca/assets/puppet/02_torço.png",
                "sprite": ""

            },
            "rightArm": {
                "status": True,
                "asset": "forca/assets/puppet/03_perna_direita.png",
                "sprite": ""

            },
            "leftArm": {
                "status": True,
                "asset": "forca/assets/puppet/04_perna_esquerda.png",
                "sprite": ""
            },
            "rightLeg": {
                "status": True,
                "asset": "forca/assets/puppet/05_braço_direito.png",
                "sprite": ""
            },
            "leftLeg": {
                "status": True,
                "asset": "forca/assets/puppet/06_braço_esquerdo.png",
                "sprite": ""
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
        i = 0
        for key, value in self.bodyParts.items():
            if value["status"]:
                i += 1
        return i

    def bodyPartRemover(self):
        for key, value in self.bodyParts.items():
            if value["status"]:
                value["status"] = False
                if not puppet.has(value["sprite"]):
                  puppet.add(value["sprite"])
                break
        
class Game():
    def __init__(self, puppetInstance):
        self.word = ""
        self.words = ["gabriel", "python", "hangman", "developer"]  # Add more words here
        self.pannel = []
        self.puppetInstance = puppetInstance
        self.guessedLetters = set()  # Keep track of guessed letters

    def startGame(self):
        """Initializes a new game."""
        # Select a random word
        self.word = random.choice(self.words)
        print(f"New word selected: {self.word}")  # Debugging output

        # Reset the panel
        self.pannel = self.resetPannel()

        # Reset all body parts' statuses to True
        self.resetBodyParts()

        # Clear the guessed letters
        self.guessedLetters.clear()

    def resetPannel(self):
        """Resets the panel to a list of empty spaces."""
        return [" " for _ in range(len(self.word))]

    def resetBodyParts(self):
        """Resets all body parts' statuses to True."""
        for key, value in self.puppetInstance.bodyParts.items():
            value["status"] = True
        puppet.empty()

    
    def handleTry(self, letterTried):
        """Handles a letter guess."""
        # Check if the letter has already been guessed
        if letterTried in self.guessedLetters:
            print(f"You've already tried the letter '{letterTried}'.")
            return

        # Add the letter to the set of guessed letters
        self.guessedLetters.add(letterTried)

        print("GOT ")
        if self.isLetterPresent(letterTried):  # This code runs when the user guesses correctly
            print("GOT AGAIN")
            self.updatePannel(letterTried)
            self.handleVictory()
            return

        print("GOT WRONG")
        self.puppetInstance.tryGotWrong()  # Handles a wrong guess by calling Puppet methods
        self.checkGameOver()  # Check if the game is over due to loss


    def isLetterPresent(self, letter):
        for e, l in enumerate(self.word):
            if letter == l:
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

    def handleLoss(self):
        """Handles the loss condition."""
        msg = "Você perdeu!!"
        size = len(msg) + 4
        print("=" * size)
        print(f"  {msg}  ")
        print("=" * size)
        print(f"A palavra era: {self.word}")  # Reveal the correct word
        self.pannel = self.resetPannel()  # Reset the panel
        self.resetBodyParts()  # Reset the puppet
        self.guessedLetters.clear()  # Clear guessed letters
        self.startGame()  # Start a new game

    def checkGameOver(self):
        """Checks if the game is over due to loss."""
        if not self.hasVictoryHappen() and self.puppetInstance.countRemainingParts() == 0:
            self.handleLoss()

class Test:
    def __init__(self):
        pass
    def testGame(self, gameInstance):
        while True:
            print(gameInstance.pannel)
            print(puppetInstance_.bodyParts)
            guess = input("Chute uma letra:")
            gameInstance.handleTry(guess)

puppetInstance_ = Puppet()
gameInstance = Game(puppetInstance_)
testInstance = Test() 

wordGroup = pygame.sprite.Group()

## LOADING FONT
pygame.font.init()
font = pygame.font.Font("forca/assets/ANDYB.TTF", 100)  # Font size is set to 40px
fontSmall = pygame.font.Font("forca/assets/ANDYB.TTF", 40)
font.set_underline(True)  # Enable underline for the font


class TextBox(pygame.sprite.Sprite):
    def __init__(self, x, y, asset):
        pygame.sprite.Sprite.__init__
        self.rect.center = ()

class WordPanel(pygame.sprite.Sprite):
    def __init__(self, x, y, font, gameInstance):
        super().__init__()
        self.x = x
        self.y = y
        self.font = font
        self.gameInstance = gameInstance
        self.image = None
        self.rect = None
        self.update()

    def update(self):
        # Fixed spacing between letters
        spacing = 70  # Adjust this value for more or less spacing
        letters = self.gameInstance.pannel

        # Create a surface to hold the entire word panel
        width = len(letters) * spacing
        height = self.font.get_height()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)  # Transparent background

        # Render each letter with fixed spacing
        for i, letter in enumerate(letters):
            letter_surface = self.font.render(letter, True, (255, 255, 255))  # White text
            self.image.blit(letter_surface, (i * spacing, 0))  # Position each letter

        # Center the panel on the specified coordinates
        self.rect = self.image.get_rect(center=(self.x, self.y))



# VIEW

pygame.init()

#define screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Groups")

#frame rate
clock = pygame.time.Clock()
FPS = 60

#create class for background
class Background(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("forca/assets/cenario.jpg")
    self.rect = self.image.get_rect()
    self.rect.center = (500, 300)

puppet = pygame.sprite.Group()

class BodyPart(pygame.sprite.Sprite):
  def __init__(self, x, y, path):
    super().__init__()
    self.image = pygame.image.load(path)
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)

# Adicionando os sprites na array de bodyPartSprites
for key, value in puppetInstance_.bodyParts.items():
  print(value)
  _ = BodyPart(150, 300, value["asset"])
  value["sprite"]  = _

screenStuff = pygame.sprite.Group()
screenStuff.add(Background())

# ADDS THE PANEL IN THE SCREEN

wordPanel = WordPanel(500, 500, font, gameInstance)  # Centered at (500, 500)

#game loop
run = True
screenStuff.draw(screen)

# Add the WordPanel to a sprite group
wordPanelGroup = pygame.sprite.Group()
wordPanelGroup.add(wordPanel)

# Game loop



gameInstance.startGame()

def showStartScreen(screen, font):
    """Displays the start game screen."""
    screen.fill("black")  # Fill the screen with black

    # Render the "Start Game" message
    title_text = fontSmall.render("Pressione espaço para começar.", True, (255, 255, 255))  # White text
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(title_text, title_rect)

    # Update the display
    pygame.display.flip()

    # Wait for the player to press the spacebar
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

showStartScreen(screen, font)

run = True
while run:
    print(gameInstance.pannel)
    clock.tick(FPS)

    # Update background
    screen.fill("black")

    # Update and draw the background and other elements
    screenStuff.update()
    screenStuff.draw(screen)

    # Update and draw the WordPanel
    wordPanelGroup.update()
    wordPanelGroup.draw(screen)

    # Update and draw the puppet
    puppet.update()
    puppet.draw(screen)

    # Event handler
    for event in pygame.event.get():
        # Quit program
        if event.type == pygame.QUIT:
            run = False

        # Handle key presses for letter tries
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():  # Check if the key pressed is a letter
                guessed_letter = event.unicode.lower()  # Convert to lowercase
                gameInstance.handleTry(guessed_letter)  # Pass the guessed letter to the game logic

    # Update display
    pygame.display.flip()

pygame.quit()

class Fork(pygame.sprite.Sprite):
    """Class to represent the gallows (forca)."""
    def __init__(self, x, y):
        super().__init__()
        # Load the gallows image
        self.image = pygame.image.load("forca/assets/forca/forca corda.png").convert_alpha()
        self.rect = self.image.get_rect()
        # Position the gallows
        self.rect.center = (x, y)