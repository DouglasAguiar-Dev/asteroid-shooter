import sys # Import the sys module
import pygame # Import the pygame module 

def laser_update(laser_list, speed = 300): # define a function to update the position of the lasers in the list
    for laser in laser_list: # iterate through the list of laser rectangles
        laser.y -= speed * dt # move the laser up by the specified speed multiplied by the time since the last frame
        if laser.bottom < 0: # check if the bottom of the laser is above the top of the window
            laser_list.remove(laser) # remove the laser from the list if it is above the top of the window

# game init
pygame.init() 
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720 # Set the width and height of the window to 1280 and 720 pixels respectively
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Get the display surface and shown on the screen with the specified width and height
pygame.display.set_caption("Asteroids Shooter") # get the caption of the window and set it to "Asteroids Shooter"
clock = pygame.time.Clock() # create a clock object to control the frame rate of the game

# ship import 
ship_surf = pygame.image.load("assets/graphics/ship.png").convert_alpha() # load the ship image and convert it to a format that pygame can us
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)) # get the rectangle of the ship image and set its center to the center of the window

# laser import
laser_surf = pygame.image.load("assets/graphics/laser.png").convert_alpha() # load the laser image and convert it to a format that pygame can use
laser_list=[] # create an empty list to store the laser rectangles
laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop) # get the rectangle of the laser image and set its midbottom to the midtop of the ship rectangle

# background import
background_surf = pygame.image.load("assets/graphics/background.png").convert_alpha() # load the background image and convert it to a format that pygame can use

# import fonts
font = pygame.font.Font("assets/graphics/subatomic.ttf", 50) # load the font and set the size to 50
text_surf = font.render("Asteroids Shooter", True, (255, 255, 255)) # render the text to a surface with the specified color
text_rect = text_surf.get_rect(midtop=(WINDOW_WIDTH / 2, 100)) # get the rectangle of the text surface and set its midtop to the center of the window and 100 pixels from the top

while True:
   
    # event loop 
    for event in pygame.event.get(): # get all the events that have happened since the last time this function was called
        if event.type == pygame.QUIT: # check if the event is a quit event
            pygame.quit() # quit pygame
            sys.exit() # the code will stop running after this line, so we need to call sys.exit() to exit the program
        
        if event.type == pygame.MOUSEBUTTONDOWN:  
            laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop) # get the rectangle of the laser image and set its midbottom to the midtop of the ship rectangle
            laser_list.append(laser_rect) # add the laser rectangle to the list of laser rectangles
    
    # frame rate control
    dt = clock.tick(120) / 1000  # set the frame rate to 120 frames per second and get the time since the last frame in seconds
    
    # mouse input handling
    ship_rect.center = pygame.mouse.get_pos() # get the position of the mouse cursor
    
    #update  
    laser_update(laser_list) # call the laser_update function to update the position of the lasers in the list

    # drawing 
    display_surface.fill((0,0,0)) # fill the display surface with color of your choice
    display_surface.blit(background_surf, (0, 0)) # draw the background image to the display surface at the top left corner
    display_surface.blit(text_surf, text_rect) # draw the text to the display surface at the top center of the screen
    
    # rect drawing
    pygame.draw.rect(display_surface, (255, 0, 0), text_rect.inflate(20, 20), width=3, border_radius=10) # draw a rectangle to the display surface with the specified color and position
    for laser in laser_list: # iterate through the list of laser rectangles
        display_surface.blit(laser_surf, laser) # draw the laser image to the display surface at its position
    display_surface.blit(ship_surf, ship_rect) # draw the ship image to the display surface at its position

     # draw the final frame
    pygame.display.update() # update the display surface