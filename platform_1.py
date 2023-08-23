import pygame
from settings import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill(BLACK)
        self.rect = self.surf.get_rect(topleft = (x, y))