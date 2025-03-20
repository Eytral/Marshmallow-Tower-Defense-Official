from Constants import config, sprites
import pygame

class Bullet:
    """
    The Bullet class represents a bullet fired by a tower.
    Handles the bullet's movement, rendering, and interaction with targets.
    """
    
    def __init__(self, x_pos, y_pos, target, speed=5, damage=1):
        """
        Initializes the bullet with its properties.

        Args:
            x_pos (int): The initial x-position of the bullet.
            y_pos (int): The initial y-position of the bullet.
            target (Enemy): The enemy that the bullet is targeting.
            speed (int): The speed at which the bullet moves. Default is 5.
            damage (int): The amount of damage the bullet inflicts on the target. Default is 1.
        """
        self.target = target  # Target the bullet will follow
        self.speed = speed  # Speed at which the bullet moves
        self.damage = damage  # Amount of damage the bullet inflicts

        self.sprite = sprites.BULLET_SPRITE  # Bullet's visual representation (sprite)

        self.x_pos = x_pos  # Initial x-position of the bullet
        self.y_pos = y_pos  # Initial y-position of the bullet

        self.active = True  # Tracks whether the bullet is still active. If False, the bullet is removed.

        self.width, self.height = config.GRID_CELL_SIZE//5, config.GRID_CELL_SIZE//5  # Bullet's dimensions (scaled down from grid size)
        self.hitbox = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)  # Bullet's hitbox for collision detection

    def update(self):
        """
        Updates the bullet's state. Moves the bullet and checks if it has hit the target.

        If the bullet is not active (e.g., hit or out of bounds), it does nothing.
        """
        if not self.active:
            return  # If the bullet is inactive, stop processing its update.

        # Here, you would add logic to move the bullet and check if it reaches the target.
        # For example:
        # If the bullet reaches the target, deal damage and deactivate the bullet.

    def draw(self, screen):
        """
        Draws the bullet on the screen.

        Args:
            screen (pygame.Surface): The screen or surface where the bullet should be rendered.
        """
        screen.blit(self.sprite, (self.x_pos, self.y_pos))  # Draw the bullet's sprite at its current position

    def move(self):
        """
        Moves the bullet based on its current position and speed.

        This method could be expanded to implement specific movement logic for the bullet
        (e.g., linear, curved, or homing). It would update the x_pos and y_pos coordinates.
        """
        # Placeholder for movement logic:
        self.hitbox = pygame.Rect(self.x_pos, self.y_pos, config.GRID_CELL_SIZE//5, config.GRID_CELL_SIZE//5)
        # In this section, you would update the bullet's position using its speed or other movement logic.
