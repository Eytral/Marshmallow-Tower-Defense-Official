from Entities.Projectiles.base_projectile import Projectile
from Constants import config, sprites

class Saw(Projectile):
    def __init__(self, x_pos, y_pos, target, bullet_speed, bullet_damage):
        super().__init__(x_pos, y_pos, target, bullet_speed, bullet_damage)
        self.type="Saw"
        self.sprite=sprites.SAW_SPRITE