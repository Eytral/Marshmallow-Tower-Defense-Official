from Entities.Projectiles.base_projectile import Projectile
from Constants import config, sprites
import pygame

class Flame(Projectile):
    """
    The Flame class represents a fire-based projectile that deals area-of-effect (AoE) damage to enemies within range.
    It inherits from the base Projectile class and adds functionality for range checking and multiple enemy hits.
    """
    def __init__(self, x_pos, y_pos, target, bullet_speed, bullet_damage, range, tower_grid_pos):
        """
        Initializes a Flame projectile with specific attributes.

        Args:
            x_pos: The x-position of the flame projectile.
            y_pos: The y-position of the flame projectile.
            target: The target enemy the flame is aimed at.
            bullet_speed: The speed at which the flame travels.
            bullet_damage: The amount of damage the flame inflicts on enemies.
            range: The range within which the flame affects enemies.
            tower_grid_pos: The grid position of the tower that fired the flame.
        """
        super().__init__(x_pos, y_pos, target, bullet_speed, bullet_damage, width=config.GRID_CELL_SIZE, height=config.GRID_CELL_SIZE, bullet_sprite=sprites.FIREBALL_SPRITE)
        self.type = "Fire"  # The type of the projectile is fire
        self.range = range + range // 5  # Add extra range to the flame for more reach
        self.tower_grid_pos = tower_grid_pos  # Grid position of the tower that fired the flame
        self.enemy_hit_list = []  # List to track enemies hit by the flame

    def update(self, enemies):
        """
        Updates the state of the flame projectile, checking if it's still in range of the tower.
        
        Args:
            enemies: The list of active enemies in the game.
        """
        super().update(enemies)  # Call base class update method
        if not self.in_range():  # Check if the flame has moved out of range
            print("Flame died")  # Debugging message
            self.active = False  # Deactivate the flame if it's out of range

    def in_range(self):
        """
        Checks if the flame projectile is within the specified range of the tower's position.
        
        Returns:
            True if the flame is within range, False otherwise.
        """
        # Calculate the grid position of the flame's current location
        x_grid_pos = round(self.x_pos / config.GRID_CELL_SIZE)
        y_grid_pos = round((self.y_pos - config.SCREEN_TOPBAR_HEIGHT) / config.GRID_CELL_SIZE)
        # Check if the flame is within range of the tower's grid position
        return abs(x_grid_pos - self.tower_grid_pos[0]) <= self.range and abs(y_grid_pos - self.tower_grid_pos[1]) <= self.range

    def check_collisions(self, enemies):
        """
        Checks for collisions between the flame and any enemies in its path.
        If a collision occurs, the enemy takes damage.

        Args:
            enemies: The list of enemies in the game.
        """
        for enemy in enemies:
            if enemy not in self.enemy_hit_list:  # Avoid re-hitting enemies
                if pygame.Rect.colliderect(self.hitbox, enemy.hitbox):  # Check for collision
                    enemy.take_damage(self.damage, damage_type=self.type)  # Apply damage to the enemy
                    self.enemy_hit_list.append(enemy)  # Add the enemy to the hit list to prevent multiple hits
