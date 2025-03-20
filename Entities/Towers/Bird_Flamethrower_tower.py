from Constants import sprites
from Entities.Towers.base_tower import Tower


class BirdFlamethrower(Tower):
    def __init__(self, x_grid_pos, y_grid_pos):
        super().__init__(x_grid_pos, y_grid_pos, range=1, fire_rate=20, bullet_speed=20, bullet_damage=2, cost=30)
        self.sprite = sprites.BIRDFLAMETHROWER_TOWER_SPRITE
    
    def upgrade(self):
        # upgrade logic
        pass