from Entities.Projectiles.base_projectile import Projectile
from Constants import config, sprites

class Bullet(Projectile):
    def __init__(self, x_pos, y_pos, target, bullet_speed, bullet_damage):
        super().__init__(x_pos, y_pos, target, bullet_speed, bullet_damage)