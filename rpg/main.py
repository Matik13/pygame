# Example file showing a circle moving on screen
import pygame
import os
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1366, 768))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('RPG Open World By Matik')
dt = 0
direction = 2
RYCERZ_IMAGE= pygame.image.load(os.path.join('rpg', 'Rycerz128.png'))
RYCERZR_IMAGE= pygame.image.load(os.path.join('rpg', 'Rycerz128r.png'))
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("lightblue")
    if(direction == 2):
        screen.blit(RYCERZ_IMAGE, (player_pos))
    if(direction == 3):
        screen.blit(RYCERZR_IMAGE, (player_pos))
    #pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        direction = 2
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        direction = 3

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

class Hand(pygame.sprite.Sprite):
    def __init__(self, hand_side):
        super().__init__()
        self.new_y = 0
        self.offset_x = 0
        self.side = hand_side
        self.can_score = True

        self._load_hand()
pygame.quit()