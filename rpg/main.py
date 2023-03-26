# Example file showing a circle moving on screen
import pygame
import os
import random
# pygame setup
pygame.init()
screen = pygame.display.set_mode((768, 768))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('RPG Open World By Matik')
dt = 0
direction = 2
background = pygame.image.load(os.path.join('rpg', 'background_grass.png')).convert()
background_x = 0
background_y = 0
background_width = background.get_width()
background_height = background.get_height()
background_speed = 5
CHEST = pygame.image.load(os.path.join('rpg', 'chest.png'))
chest_x =random.randint(-100,100)
chest_y =random.randint(-100,100)
WARRIOR_RIGHT_IMAGE= pygame.image.load(os.path.join('rpg', 'warrior_right.png'))
WARRIOR_LEFT_IMAGE= pygame.image.load(os.path.join('rpg', 'warrior_left.png'))
player_pos = pygame.Vector2(screen.get_width() / 2 -32, screen.get_height() / 2 - 32)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("lightblue")
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        background_y += background_speed
        chest_y += background_speed
    if keys[pygame.K_s]:
        background_y -= background_speed
        chest_y -= background_speed
    if keys[pygame.K_a]:
        background_x += background_speed
        chest_x += background_speed
        direction = 2
    if keys[pygame.K_d]:
        background_x -= background_speed
        chest_x -= background_speed
        direction = 3

    # Obliczenie pozycji tła w nieskończoność
    background_x = background_x % background_width
    background_y = background_y % background_height

    # Wyświetlenie tła
    screen.blit(background, (background_x, background_y))
    screen.blit(background, (background_x - background_width, background_y))
    screen.blit(background, (background_x, background_y - background_height))
    screen.blit(background, (background_x - background_width, background_y - background_height))
    screen.blit(CHEST, (chest_x, chest_y) )
    if(direction == 2):
        screen.blit(WARRIOR_LEFT_IMAGE, (player_pos))
    if(direction == 3):
        screen.blit(WARRIOR_RIGHT_IMAGE, (player_pos))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
pygame.quit()