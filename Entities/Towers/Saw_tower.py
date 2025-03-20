from Constants import sprites
from Entities.Towers.base_tower import Tower

class Saw(Tower):
    def __init__(self, x_grid_pos, y_grid_pos):
        super().__init__(x_grid_pos, y_grid_pos, range=1, fire_rate=5, bullet_speed=100, bullet_damage=2, cost=40)
        self.sprite = sprites.SAW_TOWER_SPRITE

    def upgrade(self):
        # upgrade logic
        pass