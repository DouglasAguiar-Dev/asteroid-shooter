import sys # Import the sys module
import pygame # Import the pygame module 
from random import randint, uniform # Import the randint and uniform functions from the random module
 
def display_score(): # define a function to display the score on the screen
    score = f'Score: {pygame.time.get_ticks() // 1000}' # get the current time in seconds since the game started and format it as a string
    text_surf = font.render(score, True, (255, 255, 255)) # render the text to a surface with the specified color
    text_rect = text_surf.get_rect(midtop=(WINDOW_WIDTH / 2, 100)) # get the rectangle of the text surface and set its midtop to the center of the window and 100 pixels from the top
    display_surface.blit(text_surf, text_rect) # draw the text surface to the display surface at its position
    pygame.draw.rect(display_surface, (255, 0, 0), text_rect.inflate(30, 30), width=8, border_radius=10) # draw a red rectangle around the text surface with a width of 8 pixels and a border radius of 10 pixels
  
def laser_update(laser_list, speed = 300): # define a function to update the position of the lasers in the list
    for laser in laser_list[:]: # iterate over a copy so removing items does not skip lasers
        laser.y -= speed * dt # move the laser up by the specified speed multiplied by the time since the last frame
        if laser.bottom < 0: # check if the bottom of the laser is above the top of the window
            laser_list.remove(laser) # remove the laser from the list if it is above the top of the window

def laser_timer(can_shoot, duration = 500): # define a function to handle the shooting timer
    if not can_shoot: 
        current_time = pygame.time.get_ticks() # get the current time in milliseconds since the game started
        if current_time - shoot_timer > duration: # check if the time since the last shot was fired is greater than the specified duration
            can_shoot = True # set the can_shoot variable to True so the player can shoot again
    return can_shoot # return the can_shoot variable so it can be used in the main loop

def meteor_update(meteor_list, speed = 300): # define a function to update the position of the meteors in the list
    for meteor_tuple in meteor_list[:]: # iterate over a copy so removing items does not skip meteors
        
        direction = meteor_tuple[1] # get the direction vector of the meteor
        meteor_rect = meteor_tuple[0] # get the rectangle of the meteor
        meteor_rect.center += direction * speed * dt # move the meteor down by the specified speed multiplied by the time since the last frame
        if meteor_rect.top > WINDOW_HEIGHT: # check if the top of the meteor is below the bottom of the window
            meteor_list.remove(meteor_tuple) # remove the meteor from the list if it is below the bottom of the window
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

# laser timer
can_shoot = True # create a variable to store whether the player can shoot or not
shoot_timer = None # create a variable to store the time since the last shot was fired

# background import
background_surf = pygame.image.load("assets/graphics/background.png").convert_alpha() # load the background image and convert it to a format that pygame can use

# import fonts
font = pygame.font.Font("assets/graphics/subatomic.ttf", 50) # load the font and set the size to 50

# import meteor 
meteor_surf = pygame.image.load("assets/graphics/meteor.png").convert_alpha() # load the meteor image and convert it to a format that pygame can use
meteor_list = [] # create an empty list to store the meteor rectangles

# meteor timer 
meteor_timer = pygame.event.custom_type() # create a custom event type for the meteor timer
pygame.time.set_timer(meteor_timer, 500) # set the timer for the meteor timer event to 400 milliseconds
while True:
   
    # event loop 
    for event in pygame.event.get(): # get all the events that have happened since the last time this function was called
        if event.type == pygame.QUIT: # check if the event is a quit event
            pygame.quit() # quit pygame
            sys.exit() # the code will stop running after this line, so we need to call sys.exit() to exit the program
        
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot: # check if the event is a mouse button down event
            # laser shooting
            laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop) # get the rectangle of the laser image and set its midbottom to the midtop of the ship rectangle
            laser_list.append(laser_rect) # add the laser rectangle to the list of laser rectangles

            # timer for shooting
            can_shoot = False # set the can_shoot variable to False so the player can't shoot again until the timer is up
            shoot_timer = pygame.time.get_ticks() # get the current time in milliseconds since the game
        
        if event.type == meteor_timer: # check if the event is a meteor timer event
            x_pos = randint(-100, WINDOW_WIDTH + 100) # get a random x position between -100 and WINDOW_WIDTH + 100 pixels
            y_pos = randint(-100, -50) # get a random y position between -100 and -50 pixels
            
            meteor_rect = meteor_surf.get_rect(center = (x_pos, y_pos)) # get the rectangle of the meteor image and set its center to the random x and y positions
            
            direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1) # random drift left/right while falling downward
            
            meteor_list.append((meteor_rect, direction)) # add the meteor rectangle and direction to the list of meteor rectangles
    

    
    # frame rate control
    dt = clock.tick(120) / 1000  # set the frame rate to 120 frames per second and get the time since the last frame in seconds
    
    # mouse input handling
    ship_rect.center = pygame.mouse.get_pos() # get the position of the mouse cursor
    
    # update  
    laser_update(laser_list) # call the laser_update function to update the position of the lasers in the list
    meteor_update(meteor_list) # call the meteor_update function to update the position of the meteors in the list
    can_shoot = laser_timer(can_shoot, 500) # call the laser_timer function to handle the shooting timer with a duration of 400 milliseconds

    # drawing 
    display_surface.fill((0,0,0)) # fill the display surface with color of your choice
    display_surface.blit(background_surf, (0, 0)) # draw the background image to the display surface at the top left corner
    
    display_score() # call the display_score function to display the score on the screen

    for rect in laser_list: # iterate through the list of laser rectangles
        display_surface.blit(laser_surf, rect) # draw the laser image to the display surface at its position
    
    for meteor_tuple in meteor_list: # iterate through the list of meteor rectangles
        display_surface.blit(meteor_surf, meteor_tuple[0]) # draw the meteor image to the display surface at its position

    display_surface.blit(ship_surf, ship_rect) # draw the ship on top of everything else

    pygame.display.update() # update the display surface