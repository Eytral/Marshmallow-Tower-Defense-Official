from Constants import sprites, config
import copy
import pygame
from abc import ABC

class Enemy(ABC):
    """
    The base class for all enemy types in the game.
    Inherited by specific enemy types to define movement, behavior, and damage handling.
    """

    def __init__(self, start_position, end_position, path, reward=5, health=10, speed=2):
        """
        Initializes the enemy with its properties.

        Args:
            start_position (tuple): Initial position (x, y) where the enemy is placed.
            end_position ()
            reward (int): The reward points when the enemy is killed. Default is 5.
            health (int): The total health of the enemy. Default is 10.
            speed (int): The movement speed of the enemy. Default is 2.
        """
        self.reward = reward  # Reward points when the enemy is killed
        self.max_health = health  # Maximum health of the enemy
        self.damage = self.max_health // 2  # Damage is half the max health for the enemy (example logic)
        self.speed = speed  # Movement speed

        # Position and grid position calculation
        self.position = [copy.deepcopy(start_position[0]) * config.GRID_CELL_SIZE, 
                              copy.deepcopy(start_position[1]) * config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT]  # Convert position to grid
        self.grid_position = copy.deepcopy(start_position)  # Deep copy of starting position to avoid side effects

        self.start_position = copy.deepcopy(start_position) # Stub for start position grid coords

        self.end_position = [copy.deepcopy(end_position[0]) * config.GRID_CELL_SIZE, # Deep copy of starting position to avoid side effects
                              copy.deepcopy(end_position[1]) * config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT] # Stub for end position grid coords

        self.width, self.height = config.GRID_CELL_SIZE, config.GRID_CELL_SIZE  # Set width and height based on grid size
        self.hitbox = pygame.Rect(self.position[0], self.position[1], self.width, self.height)  # Hitbox for collision detection

        self.health = self.max_health  # Set current health to max health
        self.is_dead = False  # Track if the enemy is dead
        self.reached_end = False  # Track if the enemy has reached the end of its path
        self.sprite = sprites.ENEMY_DEFAULT_SPRITE  # Default sprite for the enemy


        self.path = path

    def move(self):
        """
        Moves the enemy based on its speed. This should be expanded with logic
        that dictates the movement along the path or grid.
        """
        for _ in range(self.speed):
            
            self.position[1] += 1

            self.grid_position = self.position[0] // config.GRID_CELL_SIZE, self.position[1] // config.GRID_CELL_SIZE
            self.hitbox = pygame.Rect(self.position[0], self.position[1], config.GRID_CELL_SIZE, config.GRID_CELL_SIZE)  # Update hitbox position

            self.check_has_reached_end() # Checks if enemy has reached end

    def draw(self, screen):
        """
        Draws the enemy on the screen.

        Args:
            screen (pygame.Surface): The screen or surface to draw the enemy on.
        """
        screen.blit(self.sprite, (self.position))  # Blit (draw) the sprite at the current position

    def take_damage(self, damage, **kwargs):
        """
        Handles damage taken by the enemy.

        Args:
            damage (int): The amount of damage taken by the enemy.
            **kwargs: Additional parameters that might be passed (e.g., from specific tower effects).
        """
        print(f"Enemy taken {damage} damage")  # Print damage message for debugging
        self.health -= damage  # Decrease the enemy's health by the damage amount

    def check_is_dead(self):
        """
        Checks if the enemy is dead (health <= 0). If dead, calls the die() method.
        """
        if self.health <= 0:
            self.die()  # Calls the die() method to handle death logic

    def die(self):
        """
        Handles the enemy's death logic (set it as dead).
        """
        self.is_dead = True  # Set the enemy as dead
        print(f"Enemy has reached end (of its life)")  # Print message for debugging

    def update(self):
        """
        Updates the enemy state (e.g., movement, health checks).
        """
        self.move()  # Moves the enemy
        self.check_is_dead()  # Checks if the enemy is dead

    def check_has_reached_end(self):
        """
        Checks if the enemy has reached the end position
        """
        if self.position == self.end_position:
            self.reached_end = True
