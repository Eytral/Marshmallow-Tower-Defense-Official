from Constants import config, sprites
import pygame
import math

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

        # Predict where the enemy will be
        self.target_x, self.target_y = self.predict_enemy_position()

        # Compute velocity to move toward predicted position
        self.vx, self.vy = self.get_bullet_velocity()

        self.hitbox = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)  # Bullet's hitbox for collision detection

    def get_bullet_velocity(self):
        """ Compute velocity vector to move toward predicted target position. """
        dir_x = self.target_x - self.x_pos
        dir_y = self.target_y - self.y_pos

        magnitude = math.sqrt(dir_x**2 + dir_y**2)
        if magnitude == 0:  
            return 0, 0  # Avoid division by zero

        # Scale by bullet speed
        return (dir_x / magnitude) * self.speed, (dir_y / magnitude) * self.speed

    def update(self):
        """ Move the bullet and check if it reaches the target. """
        if not self.active:
            return

        self.x_pos += self.vx
        self.y_pos += self.vy
        self.hitbox = pygame.Rect(self.x_pos, self.y_pos, config.GRID_CELL_SIZE//5, config.GRID_CELL_SIZE//5)

    def draw(self, screen):
        """ Render the bullet on screen. """
        screen.blit(self.sprite, (self.x_pos, self.y_pos))

    def predict_enemy_position(self):
        """ Predict where the enemy will be when the bullet reaches it using iterative correction. """
        # Get current and previous enemy positions
        enemy_x, enemy_y = self.target.centre_position  # Current position
    # print(f"bullet think enemyx is {enemy_x} and enemy is {enemy_y}")
        prev_enemy_x, prev_enemy_y = self.target.prev_centre_position

        # Estimate enemy velocity
        enemy_vx = enemy_x - prev_enemy_x  # Change in x
        enemy_vy = enemy_y - prev_enemy_y  # Change in y

        # Distance to current enemy position
        distance = math.sqrt((enemy_x - self.x_pos) ** 2 + (enemy_y - self.y_pos) ** 2)
        
        # Time for bullet to reach the enemy's predicted position
        time_to_target = distance / self.speed

        # Iteratively adjust the prediction
        for _ in range(5):  # Run several iterations to refine the prediction
            # Predict enemy's future position based on its velocity
            predicted_x = enemy_x + enemy_vx * time_to_target
            predicted_y = enemy_y + enemy_vy * time_to_target

            # Calculate the distance from the tower to the predicted point
            distance = math.sqrt((predicted_x - self.x_pos) ** 2 + (predicted_y - self.y_pos) ** 2)
            
            # Recalculate time-to-target for the bullet to reach the new predicted position
            time_to_target = distance / self.speed

            # Update the enemy's predicted position
            enemy_x = predicted_x
            enemy_y = predicted_y

        return predicted_x, predicted_y
