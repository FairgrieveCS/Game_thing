import pygame
from settings import *
from pygame.locals import *

pygame.init()

# Set up screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Platformer")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Clear screen     
    screen.fill(WHITE)

    # Draw here
    pygame.display.update()

    # FPS
    clock.tick(FPS)


pygame.quit()
