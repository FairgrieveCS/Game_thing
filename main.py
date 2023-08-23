import pygame
from settings import *
from player import Player
from platform_1 import Platform
from pygame.locals import *


pygame.init()

# Set up screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Platformer")
clock = pygame.time.Clock()

player = Player()
platforms = pygame.sprite.Group()

# Create platforms
platforms.add(Platform(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40))
platforms.add(Platform(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT * 3 / 4, 100, 20))


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
                
    pressed_keys = pygame.key.get_pressed()
    player.move(pressed_keys)
    player.update(platforms)

    # Screen
    screen.fill(WHITE)
    screen.blit(player.surf, player.rect)
    for platform in platforms:
        screen.blit(platform.surf, platform.rect)

    # Draw here
    pygame.display.flip()

    # FPS
    clock.tick(FPS)


pygame.quit()
