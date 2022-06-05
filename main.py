'''
Name: Rayyan Aamir
Date: June 5, 2022
Program: Pong
'''

# Modules
import pygame

pygame.init() # Initialize

# Create window
window = pygame.display.set_mode((750, 750)) # Dimensions
pygame.display.set_caption('Pong') # Title

# Set some colour variables
white = (255, 255, 255)
black = (0, 0, 0)

gameIsDone = False

while not gameIsDone:
  pygame.time.delay(100) # In milliseconds

  # For key press, mouse click, etc
  for event in pygame.event.get():
    if event.type == pygame.QUIT: # Exit
      gameIsDone = True
      
pygame.quit()
