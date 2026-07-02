import pygame
import sys
from random import randint, uniform

class Ship (pygame.sprite.Sprite): # this is the Ship class that inherits from pygame.sprite.Sprite
    def __init__(self, groups): # this is the constructor method for the Ship class
        super().__init__(groups) #this calls the constructor of the parent class (pygame.sprite.Sprite)
        self.image = pygame.image.load("assets/graphics/ship.png").convert_alpha() # this loads the ship image and converts it to a format that is faster to blit
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50))
        self.mask = pygame.mask.from_surface(self.image) # this creates a mask for the ship image that will be used for collision detection
        self.can_shoot = True
        self.shoot_time = None 
        self.laser_sound = pygame.mixer.Sound("assets/sounds/laser.ogg") # this loads the laser sound effect and converts it to a format that is faster to play
    
    def input_position(self): # this is a method that updates the position of the ship based on the mouse position
        pos = pygame.mouse.get_pos() # this gets the current position of the mouse
        self.rect.center = pos # this sets the center position of the ship to the mouse position

    def laser_shoot(self): # this is a method that creates a laser object and adds it to the laser group
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            self.can_shoot = False  
            self.shoot_time = pygame.time.get_ticks()
            Laser(self.rect.midtop, laser_group)
            self.laser_sound.play() # this plays the laser sound effect when the ship shoots a laser
    
    def laser_timer(self): # this is a method that checks if the ship can shoot based on the last time it shot and the duration between shots
        if not self.can_shoot: 
            current_time = pygame.time.get_ticks() 
            if current_time - self.shoot_time > 800:
                self.can_shoot = True

    def meteor_collision(self): # this is a method that checks if the ship collides with any meteor in the meteor group
       if pygame.sprite.spritecollide(self, meteor_group, True, pygame.sprite.collide_mask): # this checks if the ship collides with any meteor in the meteor group and removes the meteor if it does 
            pygame.quit() # this quits the game if the ship collides with a meteor
            sys.exit() # this exits the program if the ship collides with a meteor
    
    def update(self): # this is a method that updates the ship's position
        self.laser_timer()
        self.input_position() # this calls the input_position method to update the ship's position based on the mouse position 
        self.laser_shoot() # this calls the laser_shoot method to check if the left mouse button is pressed
        self.meteor_collision() # this calls the meteor_collision method to check if the ship collides with any meteor in the meteor group

class Laser (pygame.sprite.Sprite): # this is the laser class that inherits from pygame.sprite.Sprite
    def __init__(self, pos, groups): # this is the constructor method for the laser class
        super().__init__(groups) #this calls the constructor of the parent class (pygame.sprite.Sprite)
        self.image = pygame.image.load("assets/graphics/laser.png").convert_alpha() # this loads the laser image and converts it to a format that is faster to blit
        self.rect = self.image.get_rect(midbottom = pos)
        self.mask = pygame.mask.from_surface(self.image) # this creates a mask for the laser image that will be used for collision detection
        # float based position for more accurate movement
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0,-1)
        self.speed = 600
        #sound
        self.explosion_sound = pygame.mixer.Sound("assets/sounds/explosion.wav")

    def meteor_collision(self): # this is a method that checks if the laser collides with any meteor in the meteor group
        if pygame.sprite.spritecollide(self, meteor_group, True, pygame.sprite.collide_mask): # this checks if the laser collides with any meteor in the meteor group and removes the meteor if it does 
            self.kill() # this removes the laser from the laser group if it collides with a meteor
            self.explosion_sound.play() # this plays the explosion sound effect when the laser collides with a meteor
    
    def update(self):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        if self.rect.bottom < 0: # this checks if the laser is off the screen (above the top of the window)
            self.kill() # this removes the laser from the laser group if it is off the screen
        self.meteor_collision() # this calls the meteor_collision method to check if the laser collides with any meteor in the meteor group

class Meteor (pygame.sprite.Sprite): # this is the meteor class that inherits from pygame.sprite.Sprite
    def __init__(self, pos,groups): # this is the constructor method for the meteor class
        #basic setup
        super().__init__(groups) #this calls the constructor of the parent class (pygame.sprite.Sprite)
        meteor_surface = pygame.image.load("assets/graphics/meteor.png").convert_alpha() # this loads the meteor image and converts it to a format that is faster to blit
        meteor_size = pygame.math.Vector2 (meteor_surface.get_size()) * uniform (0.5, 1.5) # this sets the size of the meteor image to a fixed size
        self.scale_surface = pygame.transform.scale(meteor_surface, meteor_size) # this scales the meteor image to a fixed size
        self.mask = pygame.mask.from_surface(self.scale_surface) # this creates a mask for the meteor image that will be used for collision detection
        self.image = self.scale_surface
        self.rect = self.image.get_rect(center = pos)

        #float based position for more accurate movement
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(uniform(-0.5,0.5), 1)
        self.speed = randint(400,600)
        
        # rotation logic
        self.rotation = 0
        self.rotation_speed = randint(20, 50) # this sets the rotation speed of the meteor to a random value between 50 and 100 degrees per second

    def rotate(self): # this is a method that rotates the meteor image based on the rotation speed
        self.rotation += self.rotation_speed * dt
        rotated_surface = pygame.transform.rotozoom(self.scale_surface, self.rotation, 1) # this rotates the meteor image by the rotation speed and scales it to 1 (no scaling)
        self.image = rotated_surface
        self.rect = self.image.get_rect(center = self.rect.center)
        self.mask = pygame.mask.from_surface(self.image) # this creates a new mask for the rotated meteor image that will be used for collision detection
    
    def update(self):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        self.rotate()

class Score: 
    def __init__(self): 
        self.font = pygame.font.Font("assets/graphics/subatomic.ttf", 50)
    
    def display(self):
        score_text = f"Score: {pygame.time.get_ticks() // 1000}" # this creates a string that displays the score based on the time elapsed since the game started
        text_surf = self.font.render(score_text, True, (255,255,255))
        text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 600))
        display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(display_surface, (255, 255, 255), text_rect.inflate(30, 30), width=8, border_radius=5)

# basic setup  
pygame.init() # 
WINDOW_WIDTH, WINDOW_HEIGHT = 1280 , 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

#background
background_surf = pygame.image.load("assets/graphics/background.png").convert_alpha()

# sprite groups 
spaceship_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()
meteor_group = pygame.sprite.Group()

# sprite creation 
ship = Ship(spaceship_group)

#timer
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500) # this sets a timer event that will trigger every 500 milliseconds (0.5 seconds) to create a new meteor 

#score
score = Score()

#music 
bg_music = pygame.mixer.Sound("assets/sounds/music.wav")
bg_music.play(loops = -1) # this plays the background music in a loop indefinitely

#game loop 
while True: 
    # event loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == meteor_timer:
            meteor_y_pos = randint(-150,-50) # this generates a random y position for the meteor between -150 and -50 (off screen)
            meteor_x_pos = randint(-100, WINDOW_WIDTH + 100) # this generates a
            Meteor((meteor_x_pos, meteor_y_pos), groups = meteor_group) # this creates a new meteor object and adds it to the meteor group when the timer event is triggered 
    
    #delta time
    dt = clock.tick(120) / 1000   
    
    # update
    display_surface.blit(background_surf, (0, 0))

    spaceship_group.update()
    laser_group.update()
    meteor_group.update()
    
    #score update
    score.display()

    spaceship_group.draw(display_surface)
    laser_group.draw(display_surface)
    meteor_group.draw(display_surface)
    pygame.display.update()