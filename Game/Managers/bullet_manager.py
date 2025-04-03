import pygame
from Constants import config

class BulletManager():
    def __init__(self, game_state):
        self.game_state = game_state
        self.bullets = []
        
    def check_bullet_collisions(self):
        """Check for bullet collisions with enemies and apply damage if hit."""
        for bullet in self.bullets:
            bullet.update(self.game_state.enemy_manager.enemies)

        self.bullets = [bullet for bullet in self.bullets if bullet.active]


    def draw_bullets(self, screen):
        """Draw all bullets on the screen"""
        for bullet in self.bullets:
            bullet.draw(screen)

    def draw(self, screen):
        self.draw_bullets(screen)