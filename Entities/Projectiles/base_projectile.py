from Constants import config, sprites
import pygame
import math

class Projectile():
    """
    The Bullet class represents a bullet fired by a tower.
    Handles the bullet's movement, rendering, and interaction with targets.
    """
    
    def __init__(self, x_pos, y_pos, target, speed=5, damage=1, bullet_type="Default", width=config.GRID_CELL_SIZE//3, height=config.GRID_CELL_SIZE//3, bullet_sprite=sprites.BULLET_SPRITE):
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
        self.type = bullet_type # Type of Bullet


        self.x_pos = x_pos  # Initial x-position of the bullet
        self.y_pos = y_pos  # Initial y-position of the bullet

        self.active = True  # Tracks whether the bullet is still active. If False, the bullet is removed.

        self.width, self.height = width, height  # Bullet's dimensions (scaled down from grid size)

        # Predict where the enemy will be
        self.target_x, self.target_y = self.predict_enemy_position()

        # Compute velocity to move toward predicted position
        self.vx, self.vy = self.get_bullet_velocity()

        self.sprite=pygame.transform.scale(bullet_sprite, (self.width, self.height))
        self.hitbox = pygame.Rect(self.x_pos - self.width // 2, self.y_pos - self.height // 2, self.width, self.height)

    def get_bullet_velocity(self):
        """ Compute velocity vector to move toward predicted target position. """
        dir_x = self.target_x - self.x_pos
        dir_y = self.target_y - self.y_pos

        magnitude = math.sqrt(dir_x**2 + dir_y**2)
        if magnitude == 0:  
            return 0, 0  # Avoid division by zero

        # Scale by bullet speed
        return (dir_x / magnitude) * self.speed, (dir_y / magnitude) * self.speed

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

    def update(self, enemies):
        """ Move the bullet and check if it reaches the target. """
        self.move()
        self.check_collisions(enemies)
        
    def move(self):
        self.x_pos += self.vx
        self.y_pos += self.vy
        self.hitbox = pygame.Rect(self.x_pos - self.width // 2, self.y_pos - self.height // 2, self.width, self.height)

    def check_collisions(self, enemies):
        for enemy in enemies:
            if pygame.Rect.colliderect(self.hitbox, enemy.hitbox):  # Check collision
                enemy.take_damage(self.damage, damage_type=self.type)
                        
                self.active = False  # Mark bullet as inactive after hitting an enemy
    
    def check_out_of_bounds(self):
        if self.x_pos > config.SCREEN_SIDEBAR_WIDTH or self.x_pos < 0 or self.y_pos > config.SCREEN_HEIGHT or self.y_pos < 0:
            self.active = False

    def draw(self, screen):
        """ Render the bullet on screen. """
        screen.blit(self.sprite, (self.x_pos - self.width // 2, self.y_pos - self.height // 2))

