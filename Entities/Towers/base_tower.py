from Constants import config, sprites
from Entities.bullet import Bullet
from abc import ABC, abstractmethod

class Tower(ABC):
    """
    Base class for creating towers in the game. This class handles basic tower mechanics such as shooting, 
    targeting, range checking, and bullet creation. It also includes attributes related to tower stats.
    """
    def __init__(self, x_grid_pos, y_grid_pos, upgrade_data=None, tile_splash_radius=0, range=5, fire_rate=30, bullet_speed=10, bullet_damage=2, cost=10):
        """
        Initializes a Tower instance with the given attributes.
        
        Args:
            x_grid_pos: X grid position of the tower on the map.
            y_grid_pos: Y grid position of the tower on the map.
            range: The attack range of the tower, in grid tiles.
            fire_rate: The rate at which the tower fires (cooldown time).
            bullet_speed: The speed at which the tower's bullets travel.
            bullet_damage: The amount of damage a bullet deals.
            cost: The cost of placing the tower on the map.
        """
        self.sprite = sprites.TOWER_DEFAULT_SPRITE  # The sprite image for the tower
        self.x_grid_pos = x_grid_pos  # The X grid position
        self.y_grid_pos = y_grid_pos  # The Y grid position

        # The position in pixels for rendering the tower on the screen
        self.x_pos = x_grid_pos * config.GRID_CELL_SIZE
        self.y_pos = y_grid_pos * config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT

        self.x_centre_pos = self.x_pos + config.GRID_CELL_SIZE//2
        self.y_centre_pos = self.y_pos + config.GRID_CELL_SIZE//2

        self.shoot_cooldown = 0  # Cooldown for shooting, starts at 0
        self.target = None  # The current target that the tower is shooting at

        self.range = range  # The attack range of the tower
        self.fire_rate = fire_rate  # The fire rate (how often the tower shoots)
        self.bullet_speed = bullet_speed  # Speed of the bullet
        self.bullet_damage = bullet_damage  # Damage dealt by each bullet
        self.tile_splash_radius = tile_splash_radius # Splash radius in tiles

        self.bullets = []  # List to store the bullets fired by the tower

        self.cost = cost  # Cost to place the tower
        self.value = self.cost

        self.upgrade_level = 0
        if upgrade_data != None:
            self.upgrade_data = upgrade_data

    def draw(self, screen):
        """
        Draws the tower and its bullets on the screen.
        
        Args:
            screen: pygame display surface where the tower and bullets will be drawn.
        """
        # Draw the tower at its position on the grid
        screen.blit(self.sprite, (self.x_pos, self.y_pos))

        # Draw all the active bullets fired by the tower
        for bullet in self.bullets:
            bullet.draw(screen)

    def shoot(self):
        """
        Fires a bullet towards the target.
        """
        # Create a bullet and add it to the list of bullets
        self.bullets.append(Bullet(self.x_centre_pos, self.y_centre_pos, self.target, self.bullet_speed, self.bullet_damage, tile_splash_radius=self.tile_splash_radius))

        # Reset the cooldown to the fire rate
        self.shoot_cooldown = self.fire_rate

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

    def update(self, enemies):
        """
        Updates the tower's state: checks if it has a target, if it needs to shoot, and updates the bullets.
        
        Args:
            enemies: List of all enemies in the game.
        """
        # If the tower has no target, or the target is dead or has reached the end, find a new target
        if self.target is None or self.target.is_dead or self.target.reached_end or not self.in_range(self.target):
            self.target = self.get_target(enemies)

        # If the shoot cooldown has elapsed, shoot at the target
        if self.shoot_cooldown <= 0:
            if self.target is not None:
                self.shoot()
        else:
            # Decrease the cooldown timer
            self.shoot_cooldown -= 1
        
        # Remove bullets that are no longer active (e.g., they hit the target)
        self.bullets = [bullet for bullet in self.bullets if bullet.active]
        
        # Update all active bullets
        for bullet in self.bullets:
            bullet.update()

    def upgrade(self, money):
        """
        An abstract method for upgrading the tower. This method should be implemented by any subclass.

        Args:
            money: Amount of money the player has when attempting upgrade
        """
        if self.upgrade_level < len(self.upgrade_data):
            if money >= self.upgrade_data[f"UPGRADE {self.upgrade_level+1}"]["Cost"]:
                self.upgrade_level += 1
                self.value += self.upgrade_data[f"UPGRADE {self.upgrade_level}"]["Cost"]
                self.range = self.upgrade_data[f"UPGRADE {self.upgrade_level}"]["Range"]
                self.fire_rate = self.upgrade_data[f"UPGRADE {self.upgrade_level}"]["Fire Rate"]
                self.bullet_speed = self.upgrade_data[f"UPGRADE {self.upgrade_level}"]["Bullet Speed"]
                self.bullet_damage = self.upgrade_data[f"UPGRADE {self.upgrade_level}"]["Bullet Damage"]
                self.tile_splash_radius = self.upgrade_data[f"UPGRADE {self.upgrade_level}"].get("Splash Radius", 0)
                print(f"Tower {self} has been successfuly upgraded")
                return True, self.upgrade_data[f"UPGRADE {self.upgrade_level}"]["Cost"]
            else:
                print("Upgrade failed: Not enough money")
                return False, "Not Enough Money to Upgrade Tower"
        else:
            print("Upgrade Failed: Max Level Already!")
            return False, "Max Upgrade Level Reached"

