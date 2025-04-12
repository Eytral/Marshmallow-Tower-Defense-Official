from Entities.Projectiles.base_projectile import Projectile
from Constants import config, sprites
import pygame

class Bomb(Projectile):
    """
    The Bomb class represents a bomb projectile that deals area-of-effect damage when it collides with an enemy.
    It inherits from the base Projectile class and adds functionality for splash damage.
    """
    def __init__(self, x_pos, y_pos, target, bullet_speed, bullet_damage, tile_splash_radius):
        """
        Initializes a Bomb projectile with specific attributes.

        Args:
            x_pos: The x-position of the bomb on the screen.
            y_pos: The y-position of the bomb on the screen.
            target: The target enemy the bomb is aimed at.
            bullet_speed: The speed at which the bomb travels.
            bullet_damage: The amount of damage the bomb deals to enemies.
            tile_splash_radius: The radius of splash damage applied to nearby enemies.
        """
        super().__init__(x_pos, y_pos, target, bullet_speed, bullet_damage, bullet_sprite=sprites.BOMB_SPRITE)
        self.type = "Bomb"  # Define the type of projectile
        self.tile_splash_radius = tile_splash_radius  # Set the splash radius for area damage

    def check_collisions(self, enemies):
        """
        Checks for collisions with enemies and applies damage.

        Args:
            enemies: A list of enemies that might be affected by the bomb's explosion.
        """
        for initial_enemy in enemies:
            if pygame.Rect.colliderect(self.hitbox, initial_enemy.hitbox):  # Check for a direct collision with the initial enemy
                initial_enemy.take_damage(self.damage, damage_type=self.type)  # Apply full damage to the initial enemy

                # Apply splash damage to nearby enemies within the radius
                for enemy in enemies:
                    if enemy != initial_enemy:  # Ensure it's not the same enemy
                        splash_radius = self.tile_splash_radius * config.GRID_CELL_SIZE  # Convert splash radius to pixels
                        # Check if the enemy is within the splash radius
                        if abs(self.x_pos - enemy.position[0]) <= splash_radius or abs(self.y_pos - enemy.position[1]) <= splash_radius:
                            enemy.take_damage(self.damage // 2, damage_type=self.type)  # Apply half damage to enemies within the splash range

                self.active = False  # Deactivate the bomb after it hits the target
