from Entities.Projectiles.base_projectile import Projectile
from Constants import config, sprites

class Laser(Projectile):
    """
    The Laser class represents a specialized projectile that fires a laser beam at the target. 
    It inherits from the base Projectile class and customizes the behavior for laser-type projectiles.
    """
    def __init__(self, x_pos, y_pos, target, bullet_speed, bullet_damage):
        """
        Initializes a Laser projectile with specific attributes.
        
        Args:
            x_pos: The x-position of the laser projectile.
            y_pos: The y-position of the laser projectile.
            target: The enemy target that the laser is aimed at.
            bullet_speed: The speed at which the laser travels.
            bullet_damage: The amount of damage the laser inflicts on enemies.
        """
        super().__init__(x_pos, y_pos, target, bullet_speed, bullet_damage, bullet_sprite=sprites.LASER_SPRITE)
        self.type = "Laser"  # Set the type of the projectile as Laser
