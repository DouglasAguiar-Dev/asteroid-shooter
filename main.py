# Import the pygame module and the sys module
import pygame, sys

# Initialize pygame
pygame.init()

# Set up the display variables
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

# Get the display surface and shown on the screen with the specified width and height
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Asteroids Shooter")

# keeps our game running
while True:
    #1 input handling
    for event in pygame.event.get(): # get all the events that have happened since the last time this function was called
        if event.type == pygame.QUIT: # check if the event is a quit event
            pygame.quit() # quit pygame
            sys.exit() # the code will stop running after this line, so we need to call sys.exit() to exit the program

    #2 update game state 

    #3 draw the game state to the display surface
    pygame.display.update() # update the display surface