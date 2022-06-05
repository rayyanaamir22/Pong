'''
Name: Rayyan Aamir
Date: June 5, 2022
Program: Pong
'''

# RUN IN TERMINAL

# Modules
import pygame

pygame.init() # Initialize

# Create window
window = pygame.display.set_mode((750, 500)) # Dimensions, a 3:2 ratio looks good
pygame.display.set_caption('Pong') # Window title

# Set some colour variables
white = (255, 255, 255)
black = (0, 0, 0)

# Paddle Class
class Paddle(pygame.sprite.Sprite): # Import pygame.sprite features
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.Surface([10, 75]) # Dimensions of the object
    self.image.fill(white) # Paddle colour
    self.rect = self.image.get_rect() # Take the image and create a rectangle hitbox around it
    self.points = 0

# Ball Class
class Ball(pygame.sprite.Sprite): # Import pygame.sprite features
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface([10, 10]) # Square hitbox
    self.image.fill(white) # Ball colour
    self.rect = self.image.get_rect()

# Create paddles
paddle1 = Paddle()
paddle1.rect.x = 25 # Initial coordinates
paddle1.rect.y = 225

paddle2 = Paddle()
paddle2.rect.x = 715 # Initial coordinates
paddle2.rect.y = 225

# Create ball
pong = Ball()
pong.rect.x = 375
pong.rect.y = 250

allSprites = pygame.sprite.Group()
allSprites.add(paddle1, paddle2, pong)

def redraw():
  window.fill(black)
  allSprites.draw(window)
  pygame.display.update()

gameIsDone = False

while not gameIsDone:
  pygame.time.delay(100) # In milliseconds

  # For key press, mouse click, etc
  for event in pygame.event.get():
    if event.type == pygame.QUIT: # Exit
      gameIsDone = True

  redraw()
      
pygame.quit()
