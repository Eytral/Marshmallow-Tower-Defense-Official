from Entities.Projectiles.base_projectile import Projectile
from Constants import config, sprites

class Bullet(Projectile):
    def __init__(self, x_pos, y_pos, target, speed=5, damage=1, tile_splash_radius=0, bullet_type="Default", width=config.GRID_CELL_SIZE // 5, height=config.GRID_CELL_SIZE // 5, bullet_sprite=sprites.BULLET_SPRITE):
        super().__init__(x_pos, y_pos, target, speed, damage, tile_splash_radius, bullet_type, width, height, bullet_sprite)