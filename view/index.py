import pygame

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

#create class for squares
class Background(pygame.sprite.Sprite):
  def __init__(self, col, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("assets/cenario.jpg")
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)

class Puppet(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

#create sprite group for squares
squares = pygame.sprite.Group()

#Create group for 

#create square and add to squares group
square = Background("crimson", 500, 300)
squares.add(square)

#game loop
run = True
while run:

  clock.tick(FPS)

  #update background
  screen.fill("black")

  #update sprite group
  squares.update()

  #draw sprite group
  squares.draw(screen)

  print(squares)

  #event handler
  for event in pygame.event.get():
    #quit program
    if event.type == pygame.QUIT:
      run = False

  #update display
  pygame.display.flip()

pygame.quit()