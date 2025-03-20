from Constants import sprites
from Entities.Towers.base_tower import Tower

class Turret(Tower):
    def __init__(self, x_grid_pos, y_grid_pos):
        super().__init__(x_grid_pos, y_grid_pos, range=3, fire_rate=30, bullet_speed=15, bullet_damage=3, cost=20)
        self.sprite = sprites.TURRET_TOWER_SPRITE

    def upgrade(self):
        # upgrade logic
        pass