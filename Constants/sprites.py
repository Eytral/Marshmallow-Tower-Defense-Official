import pygame
from Constants import config
# Map Sprites------------------------------------------------------------------------------------------------------------------------
marsh_mallows_img = pygame.image.load("Assets/Maps/placeholder_map.jpeg")
MARSH_MALLOWS_SPRITE = pygame.transform.scale(marsh_mallows_img, (config.GRID_SIZE, config.GRID_SIZE))
