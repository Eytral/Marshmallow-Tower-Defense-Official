from Entities.Projectiles.base_projectile import Projectile
from Constants import config, sprites
import pygame

class Saw(Projectile):
    """
    The Saw class represents a specialized projectile that can pierce through enemies multiple times before deactivating.
    It inherits from the base Projectile class and modifies the collision and piercing behavior.
    """
    def __init__(self, x_pos, y_pos, target, bullet_speed, bullet_damage, pierce):
        """
        Initializes a Saw projectile with specific attributes, including piercing and damage.
        
        Args:
            x_pos: The x-position of the projectile.
            y_pos: The y-position of the projectile.
            target: The enemy target that the projectile is tracking.
            bullet_speed: The speed at which the projectile travels.
            bullet_damage: The amount of damage the projectile inflicts on enemies.
            pierce: The number of times the projectile can pierce through enemies.
        """
        super().__init__(x_pos, y_pos, target, bullet_speed, bullet_damage, bullet_sprite=sprites.SAW_SPRITE)
        
        self.type = "Saw"  # Type of projectile
        self.pierce = pierce  # The total number of times the projectile can pierce through enemies
        self.pierce_number = pierce  # Counter for the remaining pierce opportunities
        self.enemy_hit_list = []  # List of enemies that have already been hit by this projectile

    def check_collisions(self, enemies):
        """
        Checks for collisions with enemies and applies damage if the projectile hits them.
        The projectile pierces through enemies up to the maximum pierce count.
        
        Args:
            enemies: A list of all active enemies in the game.
        """
        for enemy in enemies:
            # If the projectile still has piercing ability
            if self.pierce_number > 0:
                if pygame.Rect.colliderect(self.hitbox, enemy.hitbox):  # Check if the projectile collides with the enemy
                    if enemy not in self.enemy_hit_list:  # Check if this enemy has already been hit
                        enemy.take_damage(self.damage, damage_type=self.type)  # Apply damage to the enemy
                        self.enemy_hit_list.append(enemy)  # Add the enemy to the hit list
                        self.pierce_number -= 1  # Decrease the pierce counter
                        print(f"Pierce number is: {self.pierce_number}")  # Debug: print current pierce count
                        print(f"Enemy hit list is {self.enemy_hit_list}")  # Debug: print enemies hit by the projectile
                    else:
                        print(f"Enemy not hit as it has been hit already by the saw: {enemy}")  # Debug: enemy already hit
            else:
                self.active = False  # Deactivate the projectile when pierce count reaches 0
