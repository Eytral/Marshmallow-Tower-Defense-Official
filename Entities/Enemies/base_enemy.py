from Constants import config
import copy
import pygame
from abc import ABC

class Enemy(ABC):
    """
    The base class for all enemy types in the game.
    Inherited by specific enemy types to define movement, behavior, and damage handling.
    """

    def __init__(self, start_position, path, sprite=None, reward=5, health=10, speed=2):
        """
        Initializes the enemy with its properties.

        Args:
            start_position (tuple): Initial position (x, y) where the enemy is placed.
            path (list): The path the enemy follows (list of grid coordinates).
            sprite (pygame.Surface): The enemy's sprite.
            reward (int): The reward points when the enemy is killed. Default is 5.
            health (int): The total health of the enemy. Default is 10.
            speed (int): The movement speed of the enemy. Default is 2.
        """
        self.sprite = sprite
        self.reward = reward
        self.max_health = health
        self.damage = self.max_health // 2
        self.speed = speed

        # Grid size and position setup
        self.width, self.height = config.GRID_CELL_SIZE, config.GRID_CELL_SIZE
        self.start_position = copy.deepcopy(start_position)
        self.position = copy.deepcopy(start_position)
        self.prev_position = copy.deepcopy(start_position)

        # Set up hitbox for collision detection
        self.hitbox = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        self.grid_position = (copy.deepcopy(self.position[0] + self.width // 2) // config.GRID_CELL_SIZE,
                              copy.deepcopy(self.position[1] + self.height // 2) // config.GRID_CELL_SIZE)
        self.centre_position = self.hitbox.center
        self.prev_centre_position = copy.deepcopy(self.centre_position)

        self.health = self.max_health
        self.active = True
        self.path = copy.deepcopy(path)

    def move(self):
        """
        Moves the enemy along its path.
        """
        for _ in range(self.speed):
            if not self.path:  # Prevent moving when there are no more path points
                return

            target_position = self.path[0]
            x1, y1 = self.position
            x2, y2 = target_position

            # Move horizontally and vertically
            if x1 < x2:
                x1 += 1
            elif x1 > x2:
                x1 -= 1

            if y1 < y2:
                y1 += 1
            elif y1 > y2:
                y1 -= 1

            # Update position and hitbox
            self.prev_position = copy.deepcopy(self.position)
            self.position = (x1, y1)
            self.centre_position = self.hitbox.center
            self.prev_centre_position = copy.deepcopy(self.centre_position)
            self.grid_position = ((x1 + self.width // 2) // config.GRID_CELL_SIZE,
                                  ((y1 + self.height // 2) - config.SCREEN_TOPBAR_HEIGHT) // config.GRID_CELL_SIZE)
            self.hitbox = pygame.Rect(self.position[0], self.position[1], config.GRID_CELL_SIZE, config.GRID_CELL_SIZE)

            if self.position == target_position:
                del self.path[0]  # Remove the reached path point
                break

    def draw(self, screen):
        """
        Draws the enemy on the screen.

        Args:
            screen (pygame.Surface): The screen to draw the enemy on.
        """
        try:
            screen.blit(self.sprite, (self.position))
        except TypeError:
            print("No Sprite Detected, cannot draw enemy")

    def take_damage(self, damage, **kwargs):
        """
        Handles damage taken by the enemy.

        Args:
            damage (int): The amount of damage taken by the enemy.
            **kwargs: Additional parameters for special damage types.
        """
        print(f"Enemy taken {damage} damage")
        self.health -= damage

        # Adjust damage dynamically based on remaining health]
        if not self.check_is_dead():
            self.update_damage()

        print(f"Enemy {self} has {self.health} health left")

    def update_damage(self):
        """Updates the enemy's damage based on its remaining health."""
        self.damage = self.health // 2 + self.max_health // 5

    def die(self, game_state):
        """
        Handles the enemy's death logic, removing it from the game.
        """
        game_state.money += self.reward
        self.remove_self()
        print(f"Enemy has died")

    def remove_self(self, game_state):
        game_state.enemy_manager.enemies.remove(self)
        self.active = False

    def attack(self, game_state):
        """Applies damage to the game state when the enemy reaches the end."""
        game_state.health -= self.damage
        self.remove_self()
        print(f"Enemy has reached end")

    def check_is_dead(self):
        """Checks if the enemy is dead based on its health."""
        return self.health <= 0

    def check_has_reached_end(self):
        """Checks if the enemy has reached the end of the path."""
        return len(self.path) == 0

    def update(self, game_state):
        """
        Updates the enemy state (movement, health checks, etc.).
        """
        if self.active:
            self.move()
            if self.check_has_reached_end():
                self.attack(game_state)

            if self.check_is_dead():
                self.die(game_state)
