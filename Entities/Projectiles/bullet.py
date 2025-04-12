from Entities.Projectiles.base_projectile import Projectile
from Constants import config, sprites

class Bullet(Projectile):
    """
    The Bullet class represents a standard projectile fired by a tower. It inherits from the base Projectile class
    and handles the basic mechanics of bullet movement and collision detection.
    """
    def __init__(self, x_pos, y_pos, target, bullet_speed, bullet_damage):
        """
        Initializes a Bullet projectile with specific attributes.

        Args:
            x_pos: The x-position of the bullet on the screen.
            y_pos: The y-position of the bullet on the screen.
            target: The target enemy the bullet is aimed at.
            bullet_speed: The speed at which the bullet travels.
            bullet_damage: The amount of damage the bullet deals to enemies.
        """
        super().__init__(x_pos, y_pos, target, bullet_speed, bullet_damage)  # Call the parent class constructor
