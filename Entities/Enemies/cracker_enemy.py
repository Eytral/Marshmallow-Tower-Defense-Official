from Entities.Enemies.base_enemy import Enemy
from Constants import sprites, config

class Cracker(Enemy):
    def __init__(self, start_position, path):
        super().__init__(start_position, path, reward=10, health=50, speed=1)
        self.sprite = sprites.CRACKER_SPRITE
        #self.broken_sprite = sprites.BROKEN_CRACKER_SPRITE

    def become_broken(self):
        if self.health <= self.health//5:
            self.speed = 2
            # self.sprite = self.broken_sprite

    def take_damage(self, damage, **kwargs):
        if 'damage_type' in kwargs:
            damage_type = kwargs['damage_type']
        if damage_type == "Fire":
            damage = 0
        super().take_damage(damage)