import pygame
from pygame.locals import *

pygame.init()

# Constraints
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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
