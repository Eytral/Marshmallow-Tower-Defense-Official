from Constants import sprites, config
import copy
import pygame
from abc import ABC

class Enemy(ABC):
    """
    The base class for all enemy types in the game.
    Inherited by specific enemy types to define movement, behavior, and damage handling.
    """

    def __init__(self, start_position, path, reward=5, health=10, speed=2):
        """
        Initializes the enemy with its properties.

        Args:
            start_position (tuple): Initial position (x, y) where the enemy is placed.
            end_position ()
            reward (int): The reward points when the enemy is killed. Default is 5.
            health (int): The total health of the enemy. Default is 10.
            speed (int): The movement speed of the enemy. Default is 2.
        """
        self.sprite = sprites.ENEMY_DEFAULT_SPRITE  # Default sprite for the enemy
        self.reward = reward  # Reward points when the enemy is killed
        self.max_health = health  # Maximum health of the enemy
        self.damage = self.max_health // 2  # Damage is half the max health for the enemy (example logic)
        self.speed = speed  # Movement speed

        self.width, self.height = config.GRID_CELL_SIZE, config.GRID_CELL_SIZE  # Set width and height based on grid size

        # Position and grid position calculation
        self.start_position = copy.deepcopy(start_position)

        self.position = copy.deepcopy(start_position)  
        self.prev_position = copy.deepcopy(start_position)

        self.hitbox = pygame.Rect(self.position[0], self.position[1], self.width, self.height)  # Hitbox for collision detection
        self.grid_position = (copy.deepcopy(start_position[0]+self.width//2)//config.GRID_CELL_SIZE, copy.deepcopy(start_position[1]+self.height//2)//config.GRID_CELL_SIZE) # Convert position to grid

        self.centre_position = self.hitbox.center
        self.prev_centre_position = copy.deepcopy(self.centre_position)

        self.health = self.max_health  # Set current health to max health
        self.active = True

        self.path = copy.deepcopy(path)

    def move(self):
        """
        Moves the enemy based on its speed. This should be expanded with logic
        that dictates the movement along the path or grid.
        """
        for _ in range(self.speed):
            target_position = self.path[0]

            x1, y1 = self.position
            x2, y2 = target_position
            
            # Move horizontally
            if x1 < x2:
                x1 += 1
            elif x1 > x2:
                x1 -= 1
            
            # Move vertically
            if y1 < y2:
                y1 += 1
            elif y1 > y2:
                y1 -= 1
            
            # Update the enemy's position
            self.prev_position = copy.deepcopy(self.position)
            self.position = (x1, y1)
            self.centre_position = self.hitbox.center
            self.prev_centre_position = copy.deepcopy(self.centre_position)
            self.grid_position = ((x1+self.width//2)//config.GRID_CELL_SIZE, ((y1+self.height//2)-config.SCREEN_TOPBAR_HEIGHT)//config.GRID_CELL_SIZE)
            self.hitbox = pygame.Rect(self.position[0], self.position[1], config.GRID_CELL_SIZE, config.GRID_CELL_SIZE)


            if self.position == target_position:
                del self.path[0]
                break


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
        if not self.check_is_dead():
            self.damage = self.health//2 + self.max_health//5 # Updates damage to scale with remaining health (plus bonus damage based on enemy toughness)
        print(f"Enemy {self} has {self.health} health left")

    def die(self, game_state):
        """
        Handles the enemy's death logic (set it as dead).
        """
        game_state.money += self.reward
        game_state.enemy_manager.enemies.remove(self)
        self.active = False
        print(f"Enemy has reached end (of its life)")  # Print message for debugging

    def attack(self, game_state):
        game_state.health -= self.damage
        game_state.enemy_manager.enemies.remove(self)
        self.active = False

    def check_is_dead(self):
        if self.health <= 0:
            return True

    def check_has_reached_end(self):
        if len(self.path) == 0:
            print(f"Enemy has reached end")
            return True

    def update(self, game_state):
        """
        Updates the enemy state (e.g., movement, health checks).
        """
        self.move()  # Moves the enemy
        if self.check_has_reached_end():
            self.attack(game_state)

        if self.check_is_dead():
            self.die(game_state)

