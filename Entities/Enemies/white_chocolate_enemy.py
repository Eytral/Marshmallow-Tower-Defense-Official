from Entities.Enemies.base_enemy import Enemy
from Constants import sprites, config

class WhiteChocolate(Enemy):
    def __init__(self, start_position, path):
        super().__init__(start_position, path, reward=10, health=30, speed=5)
        self.sprite = sprites.WHITE_CHOCOLATE_SPRITE
        # self.melted_sprite = sprites.WHITE_CHOCOLATE_MELTED_SPRITE

    def take_damage(self, damage, **kwargs):
        if 'damage_type' in kwargs:
            damage_type = kwargs['damage_type']
        if damage_type == "Fire":
            self.melt()
        super().take_damage(damage)

    def melt(self):
        self.speed = 2
        # self.sprite = self.melted_sprite