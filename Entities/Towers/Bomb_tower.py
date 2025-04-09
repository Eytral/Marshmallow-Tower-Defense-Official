from Constants import sprites
from Entities.Towers.base_tower import Tower
from Entities.Projectiles.bomb import Bomb

class BombTower(Tower):
    """
    A specific tower type that represents a Bomb tower. It inherits from the Tower base class
    and has its own unique attributes, such as range, fire rate, bullet speed, and bullet damage.
    """

    def __init__(self, x_grid_pos, y_grid_pos):
        """
        Initializes a Bomb tower with predefined attributes like range, fire rate, bullet speed,
        bullet damage, and cost. This tower uses a specific sprite for its visual representation.

        Args:
            x_grid_pos: X grid position of the tower on the map.
            y_grid_pos: Y grid position of the tower on the map.
        """
        # Initialize the parent Tower class with the given grid position and specific attributes
        tower_data = {

            "UPGRADE 0":{
                "Range": 2,
                "Attack Delay": 75,
                "Bullet Speed": 6,
                "Bullet Damage": 11,
                "Cost": 50,
                "Splash Radius": 2
            },
            
            "UPGRADE 1": {
                "Range": 2.5,
                "Attack Delay": 60,
                "Bullet Speed": 6,
                "Bullet Damage": 15,
                "Cost": 100,
                "Splash Radius": 1.5
            },

            "UPGRADE 2": {
                "Range": 2.75,
                "Attack Delay": 50,
                "Bullet Speed": 7,
                "Bullet Damage": 20,
                "Cost": 150,
                "Splash Radius": 2
            },

            "UPGRADE 3": {
                "Range": 3,
                "Attack Delay": 40,
                "Bullet Speed": 9,
                "Bullet Damage": 30,
                "Cost": 250,
                "Splash Radius": 3
            }
            }

        super().__init__(x_grid_pos, y_grid_pos, tower_data=tower_data)

        # Set the specific sprite for the Bomb tower
        self.sprite = sprites.BOMB_TOWER_SPRITE
        self.tile_splash_radius = self.tower_data["UPGRADE 0"]["Splash Radius"]

    def shoot(self, bullets):
        """
        Fires a bullet towards the target.
        """
        # Create a bullet and add it to the list of bullets
        bullets.append(Bomb(self.x_centre_pos, self.y_centre_pos, self.target, self.bullet_speed, self.bullet_damage, tile_splash_radius=self.tile_splash_radius))

        # Reset the cooldown to the fire rate
        self.shoot_cooldown = self.attack_delay

    def upgrade(self, money):
        result = super().upgrade(money)
        if result[0]:
            self.tile_splash_radius = self.tower_data[f"UPGRADE {self.upgrade_level}"]["Splash Radius"]
        return result
