import pygame
import random  # Import random for selecting a random word
import unicodedata  # Import to normalize and remove accents

# Initialize the mixer for sound
pygame.mixer.init()

# Load sound effects
correct_sound = pygame.mixer.Sound("forca/assets/sounds/correct.mp3")
wrong_sound = pygame.mixer.Sound("forca/assets/sounds/wrong.mp3")
repeated_sound = pygame.mixer.Sound("forca/assets/sounds/repeated.mp3")

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
        self.pannel = []
        self.puppetInstance = puppetInstance
        self.guessedLetters = set()  # Keep track of guessed letters
        self.currentTheme = ""  # Store the current theme

    def startGame(self):
        """Initializes a new game."""
        # Select a random theme and word
        self.words = {
            "Frutas": ["banana", "maçã", "uva", "laranja", "abacaxi"],
            "Animais": ["cachorro", "gato", "elefante", "tigre", "leão"],
            "Cores": ["vermelho", "azul", "verde", "amarelo", "roxo"],
            "Países": ["brasil", "canadá", "japão", "alemanha", "frança"],
            "Esportes": ["futebol", "basquete", "vôlei", "tênis", "natação"]
        }
        self.currentTheme, word_list = random.choice(list(self.words.items()))
        self.word = random.choice(word_list)
        print(f"New word selected: {self.word}")  # Debugging output

        # Display the theme as a hint
        print(f"Dica: {self.currentTheme}")

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
        print(puppet)

    
    def handleTry(self, letterTried):
        """Handles a letter guess."""
        # Check if the letter has already been guessed
        if letterTried in self.guessedLetters:
            print(f"You've already tried the letter '{letterTried}'.")
            repeated_sound.play() # Play the repeated sound
            return

        self.updatePannel(letterTried)

        # Add the letter to the set of guessed letters
        self.guessedLetters.add(letterTried)

        print("GOT ")
        if self.isLetterPresent(letterTried):  # This code runs when the user guesses correctly
            print("GOT AGAIN")
            correct_sound.play()  # Play the correct sound
            self.handleVictory()
            return

        print("GOT WRONG")
        wrong_sound.play()  # Play the wrong sound
        self.puppetInstance.tryGotWrong()  # Handles a wrong guess by calling Puppet methods
        self.checkGameOver()  # Check if the game is over due to loss

    def isLetterPresent(self, letter):
        """Checks if the letter is present in the word, ignoring accents."""
        normalized_letter = unicodedata.normalize('NFD', letter).encode('ascii', 'ignore').decode('utf-8')
        for e, l in enumerate(self.word):
            normalized_word_letter = unicodedata.normalize('NFD', l).encode('ascii', 'ignore').decode('utf-8')
            if normalized_letter == normalized_word_letter:
                return True
        return False
    
    def updatePannel(self, letterTried):
        """Updates the panel with the guessed letter, ignoring accents."""
        normalized_letter = unicodedata.normalize('NFD', letterTried).encode('ascii', 'ignore').decode('utf-8')
        for e, l in enumerate(self.word):
            normalized_word_letter = unicodedata.normalize('NFD', l).encode('ascii', 'ignore').decode('utf-8')
            if normalized_letter == normalized_word_letter:
                self.pannel[e] = l

    def hasVictoryHappen(self):
        for l in self.pannel:
            if l == " ":
                return False
        return True

    def handleVictory(self):
        """Handles the victory condition."""
        if self.hasVictoryHappen():
            msg = "Você venceu!!"
            size = len(msg) + 4
            print("=" * size)
            print(f"  {msg}  ")
            print("=" * size)
            self.pannel = self.resetPannel()
            self.resetBodyParts()  # Reset the puppet
            self.guessedLetters.clear()  # Clear guessed letters
            showPlayAgainScreen(screen, font, msg)  # Show the play again screen

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
        showPlayAgainScreen(screen, font, msg)  # Show the play again screen

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
        spacing = 50  # Adjust this value for more or less spacing
        letters = self.gameInstance.pannel

        # Create a surface to hold the entire word panel
        width = len(letters) * spacing
        height = self.font.get_height()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)  # Transparent background

        # Render each letter with fixed spacing
        for i, letter in enumerate(letters):
            letter_surface = renderTextWithBorder(font, letter, (255, 255, 255), (0, 0, 0))  # White text with black border
            self.image.blit(letter_surface, (i * spacing, 0))  # Position each letter

        # Center the panel on the specified coordinates
        self.rect = self.image.get_rect(center=(self.x, self.y))



# VIEW

pygame.init()

#define screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)  # Set fullscreen mode
pygame.display.set_caption("Sprite Groups")

#frame rate
clock = pygame.time.Clock()
FPS = 60

#create class for background
class Background(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("forca/assets/cenario.png")
    self.rect = self.image.get_rect()
    self.rect.center = (500, 300)

puppet = pygame.sprite.Group()


class ForkWood(pygame.sprite.Sprite):
    """Class to represent the gallows (forca)."""
    def __init__(self, x, y):
        super().__init__()
        # Load the gallows image
        self.image = pygame.image.load("forca/assets/forca/forca corda.png").convert_alpha()
        self.rect = self.image.get_rect()
        # Position the gallows
        self.rect.center = (x, y)

class ForkRope(pygame.sprite.Sprite):
    """Class to represent the rope of the gallows."""
    def __init__(self, x, y):
        super().__init__()
        # Load the rope image
        self.image = pygame.image.load("forca/assets/forca/metade da corda.png").convert_alpha()
        self.rect = self.image.get_rect()
        # Position the rope
        self.rect.center = (x, y)
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

completeFork = pygame.sprite.Group()
completeFork.add(ForkWood(150, 450))
completeFork.add(ForkRope(230, 450))    

class BodyPart(pygame.sprite.Sprite):
    def __init__(self, x, y, path):
        super().__init__()
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 1.2, self.image.get_height() // 1.2))  # Scale down by 50%
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Adicionando os sprites na array de bodyPartSprites
for key, value in puppetInstance_.bodyParts.items():
  print(value)
  _ = BodyPart(230, 570, value["asset"])
  value["sprite"]  = _

screenStuff = pygame.sprite.Group()
screenStuff.add(Background())
screenStuff.add(completeFork)  # Add the puppet group to the screenStuff group

# ADDS THE PANEL IN THE SCREEN

def renderTextWithBorder(font, text, color, border_color):
    """Renders text with a black border."""
    text_surface = font.render(text, True, color)
    border_surfaces = [
        font.render(text, True, border_color) for _ in range(8)
    ]
    offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]
    width, height = text_surface.get_size()
    bordered_surface = pygame.Surface((width + 2, height + 2), pygame.SRCALPHA)
    for border_surface, offset in zip(border_surfaces, offsets):
        bordered_surface.blit(border_surface, (1 + offset[0], 1 + offset[1]))
    bordered_surface.blit(text_surface, (1, 1))
    return bordered_surface


wordPanel = WordPanel(600, 500, font, gameInstance)  # Centered at (500, 500)

#game loop
run = True
screenStuff.draw(screen)

# Add the WordPanel to a sprite group
wordPanelGroup = pygame.sprite.Group()
wordPanelGroup.add(wordPanel)

# Game loop



gameInstance.startGame()


def showHint(screen, fontSmall, hint):
    """Displays the hint (theme) at the top of the screen with a border."""
    hint_text = renderTextWithBorder(fontSmall, f"Dica: {hint}", (255, 255, 255), (0, 0, 0))  # White text with black border
    hint_rect = hint_text.get_rect(center=(SCREEN_WIDTH // 2, 30))  # Position at the top center
    screen.blit(hint_text, hint_rect)

def showStartScreen(screen, font):
    """Displays the start game screen with a border."""
    screen.fill("black")  # Fill the screen with black

    # Render the "Start Game" message
    title_text = renderTextWithBorder(fontSmall, "Pressione espaço para começar.", (255, 255, 255), (0, 0, 0))  # White text with black border
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(title_text, title_rect)

    # Update the display
    pygame.display.flip()

def showPlayAgainScreen(screen, font, message):
    """Displays the play again screen with a message and a border."""
    screen.fill("black")  # Fill the screen with black

    # Render the end game message
    end_text = renderTextWithBorder(font, message, (255, 255, 255), (0, 0, 0))  # White text with black border
    end_rect = end_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(end_text, end_rect)

    # Render the "Play Again" instruction
    play_again_text = renderTextWithBorder(fontSmall, "Pressione espaço para jogar novamente ou ESC para sair.", (255, 255, 255), (0, 0, 0))
    play_again_rect = play_again_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    screen.blit(play_again_text, play_again_rect)

    # Update the display
    pygame.display.flip()

    # Wait for the player to press a key
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Restart the game
                    waiting = False
                elif event.key == pygame.K_ESCAPE:  # Quit the game
                    pygame.quit()
                    exit()
    gameInstance.startGame()  # Restart the game

# Example of adding themes and words

run = True
while run:
    clock.tick(FPS)

    # Update background
    screen.fill("black")

    # Update and draw the background and other elements
    screenStuff.update()
    screenStuff.draw(screen)

    # Display the hint at the top of the screen
    showHint(screen, fontSmall, gameInstance.currentTheme)

    # Update and draw the WordPanel
    wordPanelGroup.update()
    wordPanelGroup.draw(screen)

    # Update and draw the puppet
    puppet.update()
    puppet.draw(screen)

    # Draw ForkWood last to ensure it is in front
    for sprite in completeFork:
        if isinstance(sprite, ForkRope):
            screen.blit(sprite.image, sprite.rect)

    # Event handler
    for event in pygame.event.get():
        # Quit program
        if event.type == pygame.QUIT:
            run = False

        # Handle key presses for letter tries
        if event.type == pygame.KEYDOWN:
            pygame.time.delay(500)
            if event.unicode.isalpha():  # Check if the key pressed is a letter
                guessed_letter = event.unicode.lower()  # Convert to lowercase
                gameInstance.handleTry(guessed_letter)  # Pass the guessed letter to the game logic

    # Update display
    pygame.display.flip()

pygame.quit()
