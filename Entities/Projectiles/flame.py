from Entities.Projectiles.base_projectile import Projectile
from Constants import config, sprites
import pygame

class Flame(Projectile):
    def __init__(self, x_pos, y_pos, target, bullet_speed, bullet_damage, range, tower_grid_pos):
        super().__init__(x_pos, y_pos, target, bullet_speed, bullet_damage, width=config.GRID_CELL_SIZE, height=config.GRID_CELL_SIZE, bullet_sprite=sprites.FIREBALL_SPRITE)
        self.type="Fire"
        self.range = range + range//5
        self.tower_grid_pos = tower_grid_pos

    def update(self, enemies):
        super().update(enemies)
        if not self.in_range():
            print("Flame died")
            self.active = False

    def in_range(self):
        x_grid_pos = round(self.x_pos/config.GRID_CELL_SIZE)
        y_grid_pos = round((self.y_pos-config.SCREEN_TOPBAR_HEIGHT)/config.GRID_CELL_SIZE)
        return abs(x_grid_pos - self.tower_grid_pos[0]) <= self.range and abs(y_grid_pos - (self.tower_grid_pos[1])) <= self.range

    def check_collisions(self, enemies):
        for initial_enemy in enemies:
            if pygame.Rect.colliderect(self.hitbox, initial_enemy.hitbox):  # Check collision
                initial_enemy.take_damage(self.damage, damage_type=self.type)

    
