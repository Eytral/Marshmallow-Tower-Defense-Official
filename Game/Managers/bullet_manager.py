import pygame
from Constants import config

class BulletManager():
    def __init__(self, game_state):
        self.game_state = game_state
        self.bullets = []
        
    def check_bullet_collisions(self):
        """Check for bullet collisions with enemies and apply damage if hit."""
        bullets_to_remove = []
        for _, tower in self.game_state.tower_manager.towers.items():
            for bullet in self.bullets:
                for initial_enemy in self.game_state.enemy_manager.enemies:
                    if pygame.Rect.colliderect(bullet.hitbox, initial_enemy.hitbox):  # Check collision
                        initial_enemy.take_damage(tower.bullet_damage, damage_type=bullet.type)
                        if bullet.tile_splash_radius > 0:
                            for enemy in self.game_state.enemy_manager.enemies:
                                if enemy != initial_enemy:
                                    splash_radius = bullet.tile_splash_radius * config.GRID_CELL_SIZE
                                    if bullet.x_pos-enemy.position[0] <= splash_radius or bullet.y_pos-enemy.position[1] <= splash_radius:
                                        enemy.take_damage(tower.bullet_damage//2, damage_type=bullet.type)
                                
                        bullet.active = False  # Mark bullet as inactive after hitting an enemy
                        bullets_to_remove.append(bullet) # Doesn't remove bullet during iteration - prevent logic errors/inconsistent behaviour from lack of adjustment of bullet index

        self.bullets = [bullet for bullet in self.bullets if bullet not in bullets_to_remove]


    def draw_bullets(self, screen):
        """Draw all bullets on the screen"""
        for bullet in self.bullets:
            bullet.draw(screen)

    def draw(self, screen):
        self.draw_bullets(screen)