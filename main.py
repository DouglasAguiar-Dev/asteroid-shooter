# Import the pygame module and the sys module
import pygame, sys

# Initialize pygame
pygame.init()

# Set up the display variables
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

# Get the display surface and shown on the screen with the specified width and height
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# get the caption of the window and set it to "Asteroids Shooter"
pygame.display.set_caption("Asteroids Shooter")

#import images
ship_surf = pygame.image.load("assets/graphics/ship.png").convert_alpha() # load the ship image and convert it to a format that pygame can use
background_surf = pygame.image.load("assets/graphics/background.png").convert_alpha() # load the background image and convert it to a format that pygame can use

#import fonts
font = pygame.font.Font("assets/graphics/subatomic.ttf", 50) # load the font and set the size to 50
text_surf = font.render("Asteroids Shooter", True, (255, 255, 255)) # render the text to a surface with the specified color
while True:
    #1 input handling
    for event in pygame.event.get(): # get all the events that have happened since the last time this function was called
        if event.type == pygame.QUIT: # check if the event is a quit event
            pygame.quit() # quit pygame
            sys.exit() # the code will stop running after this line, so we need to call sys.exit() to exit the program

    #2 update game state 
    display_surface.fill((0,0,0)) # fill the display surface with color of your choice
    display_surface.blit(background_surf, (0, 0)) # draw the background image to the display surface at the top left corner
    display_surface.blit(ship_surf, (640, 600)) # draw the ship image to the display surface at the center of the screen
    display_surface.blit(text_surf, (370, 100)) # draw the text to the display surface at the top center of the screen

    #3 draw the game state to the display surface
    pygame.display.update() # update the display surface 