import sys # Import the sys module
import pygame # Import the pygame module 

pygame.init() # Initialize pygame

# Set up the display variables
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720 # Set the width and height of the window to 1280 and 720 pixels respectively
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Get the display surface and shown on the screen with the specified width and height
pygame.display.set_caption("Asteroids Shooter") # get the caption of the window and set it to "Asteroids Shooter"
clock = pygame.time.Clock() # create a clock object to control the frame rate of the game

#import images
ship_surf = pygame.image.load("assets/graphics/ship.png").convert_alpha() # load the ship image and convert it to a format that pygame can us
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)) # get the rectangle of the ship image and set its center to the center of the window

background_surf = pygame.image.load("assets/graphics/background.png").convert_alpha() # load the background image and convert it to a format that pygame can use

# import fonts
font = pygame.font.Font("assets/graphics/subatomic.ttf", 50) # load the font and set the size to 50
text_surf = font.render("Asteroids Shooter", True, (255, 255, 255)) # render the text to a surface with the specified color
text_rect = text_surf.get_rect(midtop=(WINDOW_WIDTH / 2, 100)) # get the rectangle of the text surface and set its midtop to the center of the window and 100 pixels from the top

while True:
    # 1 input handling
    for event in pygame.event.get(): # get all the events that have happened since the last time this function was called
        if event.type == pygame.QUIT: # check if the event is a quit event
            pygame.quit() # quit pygame
            sys.exit() # the code will stop running after this line, so we need to call sys.exit() to exit the program
      
    # 2 update game state 
    display_surface.fill((0,0,0)) # fill the display surface with color of your choice
    display_surface.blit(background_surf, (0, 0)) # draw the background image to the display surface at the top left corner
    display_surface.blit(ship_surf, ship_rect) # draw the ship image to the display surface at its position
    display_surface.blit(text_surf, text_rect) # draw the text to the display surface at the top center of the screen

    # 3 draw the game state to the display surface
    pygame.display.update() # update the display surface

     # frame rate control
    clock.tick(120) # set the frame rate to 120 frames per second

    # mouse input handling
    ship_rect.center = pygame.mouse.get_pos() # get the position of the mouse cursor
    pygame.mouse.get_pressed() # get the state of the mouse buttons