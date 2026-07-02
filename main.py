import sys
import pygame
from random import randint, uniform

def display_score():
    score = f'Score: {pygame.time.get_ticks() // 1000}'
    text_surf = font.render(score, True, (255, 255, 255))
    text_rect = text_surf.get_rect(midtop=(WINDOW_WIDTH / 2, 100))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, (255, 0, 0), text_rect.inflate(30, 30), width=8, border_radius=10)


def laser_update(laser_list, dt, speed=300):
    for laser in laser_list[:]:
        laser.y -= speed * dt
        if laser.bottom < 0:
            laser_list.remove(laser)


def laser_timer(can_shoot, last_shot, duration=500):
    if not can_shoot and last_shot is not None:
        current_time = pygame.time.get_ticks()
        if current_time - last_shot > duration:
            can_shoot = True
    return can_shoot


def meteor_update(meteor_list, dt, speed=300):
    for meteor_tuple in meteor_list[:]:
        direction = meteor_tuple[1]
        meteor_rect = meteor_tuple[0]
        meteor_rect.center += direction * speed * dt
        if meteor_rect.top > WINDOW_HEIGHT:
            meteor_list.remove(meteor_tuple)


# game init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroids Shooter")
clock = pygame.time.Clock()

# graphics
background_surf = pygame.image.load("assets/graphics/background.png").convert_alpha()
ship_surf = pygame.image.load("assets/graphics/ship.png").convert_alpha()
laser_surf = pygame.image.load("assets/graphics/laser.png").convert_alpha()
meteor_surf = pygame.image.load("assets/graphics/meteor.png").convert_alpha()
font = pygame.font.Font("assets/graphics/subatomic.ttf", 50)

# sounds
shoot_sound = pygame.mixer.Sound("assets/sounds/laser.ogg")
explosion_sound = pygame.mixer.Sound("assets/sounds/explosion.wav")
background_music = pygame.mixer.Sound("assets/sounds/music.wav")
background_music.play(loops=-1)

# game state
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
laser_list = []
meteor_list = []
can_shoot = True
shoot_timer = None

meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            laser_rect = laser_surf.get_rect(midbottom=ship_rect.midtop)
            laser_list.append(laser_rect)
            can_shoot = False
            shoot_timer = pygame.time.get_ticks()
            shoot_sound.play()

        if event.type == meteor_timer:
            x_pos = randint(-100, WINDOW_WIDTH + 100)
            y_pos = randint(-100, -50)
            meteor_rect = meteor_surf.get_rect(center=(x_pos, y_pos))
            direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)
            meteor_list.append((meteor_rect, direction))

    # frame rate control
    dt = clock.tick(120) / 1000

    # mouse input
    ship_rect.center = pygame.mouse.get_pos()

    # update
    laser_update(laser_list, dt)
    meteor_update(meteor_list, dt)
    can_shoot = laser_timer(can_shoot, shoot_timer, 500)

    # collisions
    for meteor_tuple in meteor_list:
        if ship_rect.colliderect(meteor_tuple[0]):
            pygame.quit()
            sys.exit()

    for laser in laser_list[:]:
        for meteor_tuple in meteor_list[:]:
            if laser.colliderect(meteor_tuple[0]):
                laser_list.remove(laser)
                meteor_list.remove(meteor_tuple)
                explosion_sound.play()
                break

    # drawing
    display_surface.fill((0, 0, 0))
    display_surface.blit(background_surf, (0, 0))
    display_score()

    for rect in laser_list:
        display_surface.blit(laser_surf, rect)

    for meteor_tuple in meteor_list:
        display_surface.blit(meteor_surf, meteor_tuple[0])

    display_surface.blit(ship_surf, ship_rect)
    pygame.display.update()
