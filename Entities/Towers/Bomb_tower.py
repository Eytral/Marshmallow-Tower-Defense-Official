from Constants import sprites
from Entities.Towers.base_tower import Tower

class Bomb(Tower):
    def __init__(self, x_grid_pos, y_grid_pos):
        super().__init__(x_grid_pos, y_grid_pos, range=3, fire_rate=50, bullet_speed=5, bullet_damage=10, cost=50)
        self.sprite = sprites.BOMB_TOWER_SPRITE

    def upgrade(self):
        # upgrade logic
        pass