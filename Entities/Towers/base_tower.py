from Constants import config
from Entities.Projectiles.base_projectile import Projectile
from abc import ABC
import pygame, sys

class Tower(ABC):
    """
    Base class for creating towers in the game. This class handles basic tower mechanics such as shooting, 
    targeting, range checking, and bullet creation. It also includes attributes related to tower stats.
    """
    def __init__(self, x_grid_pos, y_grid_pos, sprite=None, tower_data=None):
        """
        Initializes a Tower instance with the given attributes.
        
        Args:
            x_grid_pos: X grid position of the tower on the map.
            y_grid_pos: Y grid position of the tower on the map.
            range: The attack range of the tower, in grid tiles.
            attack_delay: The rate at which the tower fires (cooldown time).
            bullet_speed: The speed at which the tower's bullets travel.
            bullet_damage: The amount of damage a bullet deals.
            cost: The cost of placing the tower on the map.
        """
        self.sprite = sprite  # Tower Sprite
        self.x_grid_pos = x_grid_pos  # The X grid position
        self.y_grid_pos = y_grid_pos  # The Y grid position

        # The position in pixels for rendering the tower on the screen
        self.x_pos = x_grid_pos * config.GRID_CELL_SIZE
        self.y_pos = y_grid_pos * config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT

        self.x_centre_pos = self.x_pos + config.GRID_CELL_SIZE//2
        self.y_centre_pos = self.y_pos + config.GRID_CELL_SIZE//2

        self.shoot_cooldown = 0  # Cooldown for shooting, starts at 0
        self.target = None  # The current target that the tower is shooting at
        self.upgrade_level = 0

        try:
            # Extract tower stats from tower_data based on current upgrade level
            self.range = tower_data[f"UPGRADE {self.upgrade_level}"]["Range"]
            self.attack_delay = tower_data[f"UPGRADE {self.upgrade_level}"]["Attack Delay"]
            self.bullet_damage = tower_data[f"UPGRADE {self.upgrade_level}"]["Bullet Damage"]
            self.bullet_speed = tower_data[f"UPGRADE {self.upgrade_level}"]["Bullet Speed"]
            self.cost = tower_data[f"UPGRADE {self.upgrade_level}"]["Cost"]
            self.value = self.cost
        except TypeError:
            print("Received no tower_data, exiting...")
            pygame.quit()
            sys.exit()

        self.upgrade_level = 0
        if tower_data is not None:
            self.tower_data = tower_data

    def draw(self, screen):
        """
        Draws the tower on the screen.
        
        Args:
            screen: pygame display surface where the tower and bullets will be drawn.
        """
        # Draw the tower at its position on the grid
        try:
            screen.blit(self.sprite, (self.x_pos, self.y_pos))
        except TypeError:
            print("No Sprite Detected, cannot draw enemy")

    def highlight_tower_range(self, screen, **kwargs):
        """
        Highlights the attack range of the tower on the map.
        
        Args:
            screen: The screen to draw on.
            kwargs: Optional arguments for custom positioning of the range highlight.
        """
        left = self.x_pos - self.range * config.GRID_CELL_SIZE
        top = self.y_pos - self.range * config.GRID_CELL_SIZE
        width = (self.range * 2 + 1) * config.GRID_CELL_SIZE
        height = width  # Same as width since the range is a square

        if kwargs:
            left = kwargs["left"]
            top = kwargs["top"]

        # Get the map boundaries
        map_width = config.GRID_SIZE
        map_height = config.GRID_SIZE

        # Clamp the rectangle to the map's boundaries
        clamped_left = max(0, left)
        clamped_top = max(config.SCREEN_TOPBAR_HEIGHT, top)
        clamped_right = min(map_width, left + width)
        clamped_bottom = min(config.SCREEN_TOPBAR_HEIGHT + map_height, top + height)

        # Recalculate the clamped rectangle's width and height
        clamped_width = clamped_right - clamped_left
        clamped_height = clamped_bottom - clamped_top

        # Draw the clamped rectangle
        pygame.draw.rect(screen, (0, 0, 255), (clamped_left, clamped_top, clamped_width, clamped_height), 3)

    def shoot(self, bullets):
        """
        Fires a bullet towards the target.
        
        Args:
            bullets: List of active bullets to append the new bullet to.
        """
        # Create a bullet and add it to the list of bullets
        bullets.append(Projectile(self.x_centre_pos, self.y_centre_pos, self.target, self.bullet_speed, self.bullet_damage))

        # Reset the cooldown to the fire rate
        self.shoot_cooldown = self.attack_delay

    def in_range(self, enemy):
        """
        Checks if an enemy is within the tower's attack range.
        
        Args:
            enemy: The enemy object to check.
        
        Returns:
            True if the enemy is within range, False otherwise.
        """
        # Check if the enemy is within the tower's range in both x and y directions (grid units)
        return abs(enemy.grid_position[0] - self.x_grid_pos) <= self.range and abs(enemy.grid_position[1] - self.y_grid_pos) <= self.range

    def get_target(self, enemies):
        """
        Finds the first enemy in range to target.
        
        Args:
            enemies: List of all enemies in the game.
        
        Returns:
            The first enemy that is in range, or None if no enemy is in range.
        """
        for enemy in enemies:
            if self.in_range(enemy):  # Check if the enemy is within range
                return enemy
        return None  # Return None if no enemies are in range

    def update(self, enemies, bullets):
        """
        Updates the tower's state: checks if it has a target, if it needs to shoot, and updates the bullets.
        
        Args:
            enemies: List of all enemies in the game.
            bullets: List of all active bullets.
        """
        # If the tower has no target, or the target is dead or has reached the end, find a new target
        if self.target is not None:
            if not self.target.active or not self.in_range(self.target):
                self.target = self.get_target(enemies)
        else:
            self.target = self.get_target(enemies)

        # If the shoot cooldown has elapsed, shoot at the target
        if self.shoot_cooldown <= 0:
            if self.target is not None:
                self.shoot(bullets)
        else:
            # Decrease the cooldown timer
            self.shoot_cooldown -= 1

    def upgrade(self, money):
        """
        An abstract method for upgrading the tower. This method should be implemented by any subclass.

        Args:
            money: Amount of money the player has when attempting to upgrade.
        
        Returns:
            A tuple (success, message), where success is a boolean indicating whether the upgrade was successful.
        """
        if self.upgrade_level < len(self.tower_data) - 1:
            if money >= self.tower_data[f"UPGRADE {self.upgrade_level + 1}"]["Cost"]:
                self.upgrade_level += 1
                self.value += self.tower_data[f"UPGRADE {self.upgrade_level}"]["Cost"]
                self.range = self.tower_data[f"UPGRADE {self.upgrade_level}"]["Range"]
                self.attack_delay = self.tower_data[f"UPGRADE {self.upgrade_level}"]["Attack Delay"]
                self.bullet_speed = self.tower_data[f"UPGRADE {self.upgrade_level}"]["Bullet Speed"]
                self.bullet_damage = self.tower_data[f"UPGRADE {self.upgrade_level}"]["Bullet Damage"]
                print(f"Tower {self} has been successfully upgraded")
                return True, self.tower_data[f"UPGRADE {self.upgrade_level}"]["Cost"]
            else:
                print("Upgrade failed: Not enough money")
                return False, "Not Enough Money to Upgrade Tower"
        else:
            print("Upgrade Failed: Max Level Already!")
            return False, "Max Upgrade Level Reached"
