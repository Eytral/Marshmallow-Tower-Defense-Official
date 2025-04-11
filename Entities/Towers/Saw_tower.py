from Constants import sprites
from Entities.Towers.base_tower import Tower
from Entities.Projectiles.saw import Saw

class SawTower(Tower):
    """
    A specific tower type that represents a Saw tower. It inherits from the Tower base class
    and has its own unique attributes such as range, Attack Delay, bullet speed, and bullet damage.
    """

    def __init__(self, x_grid_pos, y_grid_pos):
        """
        Initializes a Saw tower with predefined attributes like range, Attack Delay, bullet speed,
        bullet damage, and cost. This tower uses a specific sprite for its visual representation.

        Args:
            x_grid_pos: X grid position of the tower on the map.
            y_grid_pos: Y grid position of the tower on the map.
        """
        # Initialize the parent Tower class with the given grid position and specific attributes
        tower_data = {

            "UPGRADE 0": {
                "Range": 2,
                "Attack Delay": 30,
                "Bullet Speed": 20,
                "Bullet Damage": 5,
                "Cost": 30,
                "Pierce": 3
            },

            "UPGRADE 1": {
                "Range": 2.5,
                "Attack Delay": 25,
                "Bullet Speed": 20,
                "Bullet Damage": 6,
                "Cost": 100,
                "Pierce": 5
            },

            "UPGRADE 2": {
                "Range": 3,
                "Attack Delay": 20,
                "Bullet Speed": 20,
                "Bullet Damage": 7,
                "Cost": 150,
                "Pierce": 8
            },

            "UPGRADE 3": {
                "Range": 3,
                "Attack Delay": 15,
                "Bullet Speed": 20,
                "Bullet Damage": 10,
                "Cost": 250,
                "Pierce": 10
            }
            }
        super().__init__(x_grid_pos, y_grid_pos, tower_data=tower_data)

        # Set the specific sprite for the Saw tower
        self.sprite = sprites.SAW_TOWER_SPRITE
        self.pierce = self.tower_data["UPGRADE 0"]["Pierce"]

    def shoot(self, bullets):
        """
        Fires a bullet towards the target.
        """
        # Create a bullet and add it to the list of bullets
        bullets.append(Saw(self.x_centre_pos, self.y_centre_pos, self.target, self.bullet_speed, self.bullet_damage, self.pierce))

        # Reset the cooldown to the Attack Delay
        self.shoot_cooldown = self.attack_delay

    def upgrade(self, money):
        result = super().upgrade(money)
        if result[0]:
            self.pierce = self.tower_data[f"UPGRADE {self.upgrade_level}"]["Pierce"]
        return result

