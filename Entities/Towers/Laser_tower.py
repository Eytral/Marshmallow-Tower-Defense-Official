from Constants import sprites
from Entities.Towers.base_tower import Tower
from Entities.bullet import Bullet

class Laser(Tower):
    """
    A specific tower type that represents a Laser tower. It inherits from the Tower base class
    and has its own unique attributes such as range, fire rate, bullet speed, and bullet damage.
    """

    def __init__(self, x_grid_pos, y_grid_pos):
        """
        Initializes a Laser tower with predefined attributes like range, fire rate, bullet speed,
        bullet damage, and cost. This tower uses a specific sprite for its visual representation.

        Args:
            x_grid_pos: X grid position of the tower on the map.
            y_grid_pos: Y grid position of the tower on the map.
        """
        # Initialize the parent Tower class with the given grid position and specific attributes
        upgrade_data = {
            "UPGRADE 1": {
                "Range": 4,
                "Fire Rate": 4,
                "Bullet Speed": 45,
                "Bullet Damage": 1.5,
                "Cost": 100
            },

            "UPGRADE 2": {
                "Range": 4,
                "Fire Rate": 3,
                "Bullet Speed": 50,
                "Bullet Damage": 2,
                "Cost": 150
            },

            "UPGRADE 3": {
                "Range": 5,
                "Fire Rate": 2,
                "Bullet Speed": 50,
                "Bullet Damage": 3,
                "Cost": 250
            }
            }
        super().__init__(x_grid_pos, y_grid_pos, upgrade_data=upgrade_data, range=4, fire_rate=5, bullet_speed=40, bullet_damage=1, cost=35)

        # Set the specific sprite for the Laser tower
        self.sprite = sprites.LASER_TOWER_SPRITE

    def shoot(self):
        """
        Fires a bullet towards the target.
        """
        # Create a bullet and add it to the list of bullets
        self.bullets.append(Bullet(self.x_centre_pos, self.y_centre_pos, self.target, self.bullet_speed, self.bullet_damage, bullet_type="Laser", bullet_sprite=sprites.LASER_SPRITE))

        # Reset the cooldown to the fire rate
        self.shoot_cooldown = self.fire_rate
