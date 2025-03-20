from Entities.Enemies.base_enemy import Enemy
from Constants import sprites, config

class Marshmallow(Enemy):
    def __init__(self, start_position, path):
        super().__init__(start_position, path, reward=5, health=10, speed=2)
        self.sprite = sprites.MARSHMALLOW_SPRITE

