from Constants import sprites
from Entities.Towers.base_tower import Tower
from Entities.Projectiles.bullet import Bullet

class TurretTower(Tower):
    """
    A specific tower type that represents a Turret tower. It inherits from the Tower base class
    and has its own unique attributes such as range, fire rate, bullet speed, and bullet damage.
    """

    def __init__(self, x_grid_pos, y_grid_pos):
        """
        Initializes a Turret tower with predefined attributes like range, fire rate, bullet speed,
        bullet damage, and cost. This tower uses a specific sprite for its visual representation.

        Args:
            x_grid_pos: X grid position of the tower on the map.
            y_grid_pos: Y grid position of the tower on the map.
        """
        # Initialize the parent Tower class with the given grid position and specific attributes
        upgrade_data = {
            "UPGRADE 1": {
                "Range": 7,
                "Fire Rate": 21,
                "Bullet Speed": 20,
                "Bullet Damage": 9,
                "Cost": 100
            },

            "UPGRADE 2": {
                "Range": 9,
                "Fire Rate": 17,
                "Bullet Speed": 22,
                "Bullet Damage": 13,
                "Cost": 150
            },

            "UPGRADE 3": {
                "Range": 9,
                "Fire Rate": 14,
                "Bullet Speed": 25,
                "Bullet Damage": 15,
                "Cost": 250
            }
            }

        super().__init__(x_grid_pos, y_grid_pos, upgrade_data=upgrade_data, range=6, fire_rate=25, bullet_speed=20, bullet_damage=6, cost=25)

        # Set the specific sprite for the Turret tower
        self.sprite = sprites.TURRET_TOWER_SPRITE

