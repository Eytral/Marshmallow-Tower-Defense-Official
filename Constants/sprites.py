import pygame
from Constants import config

# Map Sprites------------------------------------------------------------------------------------------------------------------------
marsh_mallows_img = pygame.image.load("Assets/Maps/placeholder_map.jpeg")
MARSH_MALLOWS_SPRITE = pygame.transform.scale(marsh_mallows_img, (config.GRID_SIZE, config.GRID_SIZE))

# Tower Sprites------------------------------------------------------------------------------------------------------------------------
birdflamethrower_tower_sprite = pygame.image.load("Assets/Sprites/Towers/birdflamethrower_tower.png")
BIRDFLAMETHROWER_TOWER_SPRITE = pygame.transform.scale(birdflamethrower_tower_sprite, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

bomb_tower_sprite = pygame.image.load("Assets/Sprites/Towers/bomb_tower.png")
BOMB_TOWER_SPRITE = pygame.transform.scale(bomb_tower_sprite, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

laser_tower_sprite = pygame.image.load("Assets/Sprites/Towers/laser_tower.png")
LASER_TOWER_SPRITE = pygame.transform.scale(laser_tower_sprite, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

turret_tower_sprite = pygame.image.load("Assets/Sprites/Towers/turret_tower.png")
TURRET_TOWER_SPRITE = pygame.transform.scale(turret_tower_sprite, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

saw_tower_sprite = pygame.image.load("Assets/Sprites/Towers/saw_tower.png")
SAW_TOWER_SPRITE = pygame.transform.scale(saw_tower_sprite, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

# Enemy Sprites------------------------------------------------------------------------------------------------------------------------
marshmallow = pygame.image.load("Assets/Sprites/Enemies/marshmallow.png")
MARSHMALLOW_SPRITE = pygame.transform.scale(marshmallow, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

cracker = pygame.image.load("Assets/Sprites/Enemies/cracker.png")
CRACKER_SPRITE = pygame.transform.scale(cracker, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

broken_cracker = pygame.image.load("Assets/Sprites/Enemies/broken_cracker.png")
BROKEN_CRACKER_SPRITE = pygame.transform.scale(broken_cracker, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

white_chocolate = pygame.image.load("Assets/Sprites/Enemies/white_chocolate.png")
WHITE_CHOCOLATE_SPRITE = pygame.transform.scale(white_chocolate, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

melted_white_chocolate = pygame.image.load("Assets/Sprites/Enemies/melted_white_chocolate.png")
MELTED_WHITE_CHOCOLATE_SPRITE = pygame.transform.scale(melted_white_chocolate, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

dark_chocolate = pygame.image.load("Assets/Sprites/Enemies/dark_chocolate.png")
DARK_CHOCOLATE_SPRITE = pygame.transform.scale(dark_chocolate, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

melted_dark_chocolate = pygame.image.load("Assets/Sprites/Enemies/melted_dark_chocolate.png")
MELTED_DARK_CHOCOLATE_SPRITE = pygame.transform.scale(melted_dark_chocolate, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))

smore = pygame.image.load("Assets/Sprites/Enemies/smore.png")
SMORE_SPRITE = pygame.transform.scale(smore, (config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))


# Projectile Sprites------------------------------------------------------------------------------------------------------------------------
bullet_img = pygame.image.load("Assets/Sprites/Projectiles/bullet.png")
BULLET_SPRITE = pygame.transform.scale(bullet_img, (config.GRID_CELL_SIZE//3, config.GRID_CELL_SIZE//3))

fireball_img = pygame.image.load("Assets/Sprites/Projectiles/fireball.png")
FIREBALL_SPRITE = pygame.transform.scale(fireball_img, (config.GRID_CELL_SIZE//3, config.GRID_CELL_SIZE//3))

laser_img = pygame.image.load("Assets/Sprites/Projectiles/laser.png")
LASER_SPRITE = pygame.transform.scale(laser_img, (config.GRID_CELL_SIZE//3, config.GRID_CELL_SIZE//3))

saw_img = pygame.image.load("Assets/Sprites/Projectiles/saw.png")
SAW_SPRITE = pygame.transform.scale(saw_img, (config.GRID_CELL_SIZE//3, config.GRID_CELL_SIZE//3))

bomb_img = pygame.image.load("Assets/Sprites/Projectiles/bomb.png")
BOMB_SPRITE = pygame.transform.scale(bomb_img, (config.GRID_CELL_SIZE//3, config.GRID_CELL_SIZE//3))