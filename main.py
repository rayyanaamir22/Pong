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
    self.speed = 10
    self.dx = 1 # Change in x
    self.dy = 1 # Change in y

# Create paddles
paddle1 = Paddle()
paddle1.rect.x = 25 # Initial coordinates
paddle1.rect.y = 225

paddle2 = Paddle()
paddle2.rect.x = 715 # Initial coordinates
paddle2.rect.y = 225

paddleSpeed = 50 # Speed of moving up/down the screen

# Create ball
pong = Ball()
pong.rect.x = 375
pong.rect.y = 250

allSprites = pygame.sprite.Group()
allSprites.add(paddle1, paddle2, pong)

def redraw():
  window.fill(black)
  # Title
  font = pygame.font.SysFont('Comic Sans MS', 30)
  title = font.render('PONG', False, white)
  titleRect = title.get_rect()
  titleRect.center = (750//2, 25)

  # Player 1 score
  player1Score = font.render(str(paddle1.points), False, white)
  player1Rect = player1Score.get_rect()
  player1Rect.center = (50, 50)
  window.blit(player1Score, player1Rect)

  # Player 2 score
  player2Score = font.render(str(paddle2.points), False, white)
  player2Rect = player2Score.get_rect()
  player2Rect.center = (700, 50)
  window.blit(player2Score, player2Rect)

  window.blit(title, titleRect)
  allSprites.draw(window)
  pygame.display.update()

gameIsDone = False

while not gameIsDone:
  pygame.time.delay(100) # In milliseconds

  # For key press, mouse click, etc
  for event in pygame.event.get():
    if event.type == pygame.QUIT: # Exit
      gameIsDone = True

  key = pygame.key.get_pressed()
  '''
  The top-left corner is (0,0), so to move up, the y coordinates must decrement
  '''
  if key[pygame.K_w]: # Paddle1 UP
    paddle1.rect.y -= paddleSpeed
  if key[pygame.K_s]: # Paddle1 DOWN
    paddle1.rect.y += paddleSpeed
  if key[pygame.K_UP]: # Paddle2 UP
    paddle2.rect.y -= paddleSpeed
  if key[pygame.K_DOWN]: # Paddle2 DOWN
    paddle2.rect.y += paddleSpeed

  pong.rect.x += pong.speed * pong.dx # Speed * direction
  pong.rect.y += pong.speed * pong.dy

  # Ball bounces off the top/bottom
  if pong.rect.y > 490:
    pong.dy *= -1
  if pong.rect.y < 10:
    pong.dy *= -1
  
  # Ball bounces off a SIDE
  if pong.rect.x > 740: # Paddle2 missed
    pong.rect.x, pong.rect.y = 375, 250 # Reset to centre of screen
    pong.dx *= -1
    paddle1.points += 1
  if pong.rect.x < 10: # Paddle1 missed
    pong.rect.x, pong.rect.y = 375, 250 # Reset to centre of screen
    pong.dx *= -1 
    paddle2.points += 1

  # Ball bounces off the paddles
  if paddle1.rect.colliderect(pong.rect):
    pong.dx *= -1
  if paddle2.rect.colliderect(pong.rect):
    pong.dx *= -1

  redraw()
      
pygame.quit()
