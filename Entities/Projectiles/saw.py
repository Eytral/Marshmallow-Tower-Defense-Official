from Entities.Projectiles.base_projectile import Projectile
from Constants import config, sprites
import pygame

class Saw(Projectile):
    def __init__(self, x_pos, y_pos, target, bullet_speed, bullet_damage, pierce):
        super().__init__(x_pos, y_pos, target, bullet_speed, bullet_damage, bullet_sprite=sprites.SAW_SPRITE)
        self.type="Saw"
        self.pierce = pierce
        self.pierce_number = pierce
        self.enemy_hit_list = []


    def check_collisions(self, enemies):
        for enemy in enemies:
            if self.pierce_number > 0:
                if pygame.Rect.colliderect(self.hitbox, enemy.hitbox):  # Check collision
                    if enemy not in self.enemy_hit_list:
                        enemy.take_damage(self.damage, damage_type=self.type)
                        self.enemy_hit_list.append(enemy)
                        self.pierce_number -= 1
                        print(f"pierce number is: {self.pierce_number}")
                        print(f"enemy hit list is {self.enemy_hit_list}")
                    else:
                        print(f"enemy not hit as it has been hit already by saw: {enemy}")
            else:
                self.active = False