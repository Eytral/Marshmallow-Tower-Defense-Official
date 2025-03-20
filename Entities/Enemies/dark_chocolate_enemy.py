from Entities.Enemies.base_enemy import Enemy
from Constants import sprites, config

class DarkChocolate(Enemy):
    def __init__(self, start_position, path):
        super().__init__(start_position, path, reward=20, health=30, speed=3)
        self.sprite = sprites.DARK_CHOCOLATE_SPRITE
        #self.melted_sprite = sprites.DARK_CHOCOLATE_MELTED_SPRITE
        self.armour = 5

    def take_damage(self, damage, **kwargs):
        if 'damage_type' in kwargs:
            damage_type = kwargs['damage_type']
        if damage_type == "Fire":
            self.melt()
        if self.armour != 0:
            damage = damage//self.armour
        super().take_damage(damage)

    def melt(self):
        self.speed = 1
        self.armour = 0
        # self.sprite = self.melted_sprite