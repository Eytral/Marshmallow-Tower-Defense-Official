from Constants import sprites
from Entities.Towers.base_tower import Tower
from Entities.Projectiles.laser import Laser

class LaserTower(Tower):
    """
    A specific tower type that represents a Laser tower. It inherits from the Tower base class
    and has its own unique attributes such as range, Attack Delay, bullet speed, and bullet damage.
    """

    def __init__(self, x_grid_pos, y_grid_pos):
        """
        Initializes a Laser tower with predefined attributes like range, Attack Delay, bullet speed,
        bullet damage, and cost. This tower uses a specific sprite for its visual representation.

        Args:
            x_grid_pos: X grid position of the tower on the map.
            y_grid_pos: Y grid position of the tower on the map.
        """
        # Initialize the parent Tower class with the given grid position and specific attributes
        tower_data = {

            "UPGRADE 0": {
                "Range": 3,
                "Attack Delay": 4,
                "Bullet Speed": 40,
                "Bullet Damage": 1.5,
                "Cost": 35,
            },

            "UPGRADE 1": {
                "Range": 3.25,
                "Attack Delay": 3,
                "Bullet Speed": 45,
                "Bullet Damage": 2,
                "Cost": 100
            },

            "UPGRADE 2": {
                "Range": 3.5,
                "Attack Delay": 2,
                "Bullet Speed": 50,
                "Bullet Damage": 2.5,
                "Cost": 150
            },

            "UPGRADE 3": {
                "Range": 4,
                "Attack Delay": 0,
                "Bullet Speed": 50,
                "Bullet Damage": 3.5,
                "Cost": 250
            }
            }
        super().__init__(x_grid_pos, y_grid_pos, tower_data=tower_data, sprite=sprites.LASER_TOWER_SPRITE)


    def shoot(self, bullets):
        """
        Fires a bullet towards the target.
        """
        # Create a bullet and add it to the list of bullets
        bullets.append(Laser(self.x_centre_pos, self.y_centre_pos, self.target, self.bullet_speed, self.bullet_damage))

        # Reset the cooldown to the Attack Delay
        self.shoot_cooldown = self.attack_delay
