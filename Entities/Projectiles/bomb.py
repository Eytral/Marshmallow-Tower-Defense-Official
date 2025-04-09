from Entities.Projectiles.base_projectile import Projectile
from Constants import config, sprites
import pygame

class Bomb(Projectile):
    def __init__(self, x_pos, y_pos, target, bullet_speed, bullet_damage, tile_splash_radius):
        super().__init__(x_pos, y_pos, target, bullet_speed, bullet_damage)
        self.type="Bomb"
        self.sprite=sprites.BOMB_SPRITE
        self.tile_splash_radius = tile_splash_radius

    def check_collisions(self, enemies):
        for initial_enemy in enemies:
            if pygame.Rect.colliderect(self.hitbox, initial_enemy.hitbox):  # Check collision
                initial_enemy.take_damage(self.damage, damage_type=self.type)
                for enemy in enemies:
                    if enemy != initial_enemy:
                        splash_radius = self.tile_splash_radius * config.GRID_CELL_SIZE
                        if self.x_pos-enemy.position[0] <= splash_radius or self.y_pos-enemy.position[1] <= splash_radius:
                            enemy.take_damage(self.damage//2, damage_type=self.type)
                        
                self.active = False  # Mark bullet as inactive after hitting an enemy