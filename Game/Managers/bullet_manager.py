import pygame
from Constants import config

class BulletManager():
    """
    Manages the active bullets in the game, including checking collisions and drawing bullets.
    """
    
    def __init__(self, game_state):
        """
        Initializes the BulletManager with the given game state and an empty list for active bullets.

        Args:
            game_state: The current state of the game, which contains all game data.
        """
        self.game_state = game_state
        self.bullets = []  # List to store active bullets

    def check_bullet_collisions(self):
        """
        Checks for bullet collisions with enemies and applies damage if a bullet hits an enemy.

        Loops through all active bullets, updates their position, and checks if they collide with any enemies.
        Removes inactive bullets from the list.
        """
        for bullet in self.bullets:
            bullet.update(self.game_state.enemy_manager.enemies)  # Update the position and check for collisions with enemies

        # Remove any inactive bullets (bullets that have hit an enemy or are otherwise inactive)
        self.bullets = [bullet for bullet in self.bullets if bullet.active]

    def draw_bullets(self, screen):
        """
        Draws all active bullets on the screen.

        Args:
            screen: The screen to draw the bullets on.
        """
        for bullet in self.bullets:
            bullet.draw(screen)  # Draw each bullet on the screen

    def draw(self, screen):
        """
        Draws all bullets by calling the draw_bullets method.

        Args:
            screen: The screen to draw the bullets on.
        """
        self.draw_bullets(screen)  # Draws all bullets
