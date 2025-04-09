from Constants import config, sprites
from Entities.Projectiles.base_projectile import Projectile
from abc import ABC, abstractmethod

class Tower(ABC):
    """
    Base class for creating towers in the game. This class handles basic tower mechanics such as shooting, 
    targeting, range checking, and bullet creation. It also includes attributes related to tower stats.
    """
    def __init__(self, x_grid_pos, y_grid_pos, tower_data=None, range=5, attack_delay=30, bullet_speed=10, bullet_damage=2, cost=10):
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
        self.attack_delay = attack_delay  # The fire rate (how often the tower shoots)
        self.bullet_speed = bullet_speed  # Speed of the bullet
        self.bullet_damage = bullet_damage  # Damage dealt by each bullet

        self.cost = cost  # Cost to place the tower
        self.value = self.cost

        self.upgrade_level = 0
        if tower_data != None:
            self.tower_data = tower_data

    def draw(self, screen):
        """
        Draws the tower and its bullets on the screen.
        
        Args:
            screen: pygame display surface where the tower and bullets will be drawn.
        """
        # Draw the tower at its position on the grid
        screen.blit(self.sprite, (self.x_pos, self.y_pos))

    def shoot(self, bullets):
        """
        Fires a bullet towards the target.
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
        """
        # If the tower has no target, or the target is dead or has reached the end, find a new target
        if self.target != None:
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
            money: Amount of money the player has when attempting upgrade
        """
        if self.upgrade_level < len(self.tower_data)-1:
            if money >= self.tower_data[f"UPGRADE {self.upgrade_level+1}"]["Cost"]:
                self.upgrade_level += 1
                self.value += self.tower_data[f"UPGRADE {self.upgrade_level}"]["Cost"]
                self.range = self.tower_data[f"UPGRADE {self.upgrade_level}"]["Range"]
                self.attack_delay = self.tower_data[f"UPGRADE {self.upgrade_level}"]["Attack Delay"]
                self.bullet_speed = self.tower_data[f"UPGRADE {self.upgrade_level}"]["Bullet Speed"]
                self.bullet_damage = self.tower_data[f"UPGRADE {self.upgrade_level}"]["Bullet Damage"]
                print(f"Tower {self} has been successfuly upgraded")
                return True, self.tower_data[f"UPGRADE {self.upgrade_level}"]["Cost"]
            else:
                print("Upgrade failed: Not enough money")
                return False, "Not Enough Money to Upgrade Tower"
        else:
            print("Upgrade Failed: Max Level Already!")
            return False, "Max Upgrade Level Reached"

