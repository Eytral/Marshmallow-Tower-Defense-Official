from Constants import sprites
from Entities.Towers.base_tower import Tower

class Laser(Tower):
    def __init__(self, x_grid_pos, y_grid_pos):
        super().__init__(x_grid_pos, y_grid_pos, range=5, fire_rate=10, bullet_speed=40, bullet_damage=1, cost=40)
        self.sprite = sprites.LASER_TOWER_SPRITE

    def upgrade(self):
        # upgrade logic
        pass